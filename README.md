# Inventory Collection for Ansible

[![Ansible Lint](https://github.com/nleiva/inventory/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/nleiva/inventory/actions/workflows/ansible-lint.yml)

This repository hosts my personal Ansible inventory collection.

This collection includes a JSON plugin to read an inventory from a particular JSON structure in a file.

## Included content

Click on the name of a plugin or module to view that content's documentation:

  - **Plugins**:
    - [json](docs/json.md)

## Installation and Usage

### Installing the Collection from Ansible Galaxy

Before using this collection, you need to install it with the Ansible [Galaxy](https://galaxy.ansible.com/nleiva/inventory) CLI:

  ansible-galaxy collection install nleiva.inventory --force -p collections


You can also include it in a `requirements.yml` file and install it via `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: nleiva.inventory
    version: 1.0.5
```

### Using a plugin from the Inventory Collection

You can reach the sample JSON inventory [file](hosts.json) for example via this [repository link](https://raw.githubusercontent.com/nleiva/ansible-inventory-plugin/main/hosts.json) to add it to your [inventory.yml](inventory.yml) file:

```yml
# inventory.yml
plugin: nleiva.inventory.json
link_to_inventory: https://raw.githubusercontent.com/nleiva/ansible-inventory-plugin/main/hosts.json
validate_certs: true
```

### Run an example

With the [inventory.yml](inventory.yml) file in place, you can run `ansible-inventory -i inventory.yml` to get the inventory populated:

```bash
$ ansible-inventory -i inventory.yml --graph
@all:
  |--@routers:
  |  |--@ios:
  |  |  |--sandbox-iosxe-latest-1.cisco.com
  |  |--@iosxr:
  |  |  |--sandbox-iosxr-1.cisco.com
  |  |--@nxos:
  |  |  |--sandbox-nxos-1.cisco.com
  |--@ungrouped:
```

## Publishing New Versions

We need to TAG the version with a version number greater than the latest one:

```
export TAG=1.0.6
```

And then build:

```
make build
```

It will end up in the [Inventory collection Galaxy page](https://galaxy.ansible.com/nleiva/inventory) if you have access to the namespace.

## More Information

For more information about Inventory plugins, check out the resources in this [list](https://github.com/nleiva/ansible-links#inventory-plugins).


## License

GNU General Public License v3.0 or later

See [LICENCE](LICENSE) to see the full text.