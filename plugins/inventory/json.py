from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
    name: nleiva.inventory.json
    plugin_type: inventory
    short_description: Inventory plugin demo
    description: My Ansible inventory plugin demo
    options:
      plugin:
          description: Name of the plugin
          required: true
          choices: ['nleiva.inventory.json']
      link_to_inventory:
        description: Location of the inventory
        required: true
      validate_certs:
        description: Verify SSL certificate if using HTTPS
        type: boolean
        default: false
'''

from distutils.version import LooseVersion

from ansible.plugins.inventory import BaseInventoryPlugin, Cacheable
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.module_utils._text import to_text

# Third party imports
try:
    import requests
    if LooseVersion(requests.__version__) < LooseVersion('2.0.0'):
        raise ImportError
except ImportError:
    raise AnsibleError('This script requires python-requests 2.0 as a minimum version')


class InventoryModule(BaseInventoryPlugin):
    NAME = 'nleiva.inventory.json'

    def __init__(self):

        super(InventoryModule, self).__init__()

        self.my_url = None
        self.session = None

    def verify_file(self, path):
        ''' return true/false if this is possibly a valid file for this plugin to consume '''
        valid = False
        if super(InventoryModule, self).verify_file(path):
            if path.endswith(('.yaml', '.yml')):
                valid = True
            else:
                self.display.vvv('Skipping, inventory source files does not end in ".yaml" nor ".yml"')
        return valid

    def _get_session(self):
        if not self.session:
            self.session = requests.session()
            self.session.verify = self.get_option('validate_certs')
        return self.session

    def _get_json(self, url):
        s = self._get_session()

        response = s.get(url)

        response.raise_for_status()

        return response.json()

    def _parse_group(self, host, os):
        group = os.split(".")[-1]
        try:
            group = self.inventory.add_group(group)
        except AnsibleError as e:
            raise AnsibleParserError("Unable to add group %s: %s" % (group, to_text(e)))

        self.inventory.add_child(group, host)


    def _populate(self):

        for host in self._get_json("%s" % self.my_url):
            host_name = self.inventory.add_host(host.get('name'))
            
            vars = host
            self._parse_group(vars['name'], vars['network_os'])
            
            del vars['name']
            for key, value in vars.items():
                self.inventory.set_variable(host_name, key, value)


    def parse(self, inventory, loader, path, cache=True):
        ''' Return dynamic inventory from source '''
        
        super(InventoryModule, self).parse(inventory, loader, path)

        # read config from file, this sets 'options'
        self._read_config_data(path)

        # get connection host
        self.my_url = self.get_option('link_to_inventory')

        # submit the parsed data to the inventory object (add_host, set_variable, etc)
        self._populate()