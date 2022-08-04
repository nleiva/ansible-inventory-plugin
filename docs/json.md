## JSON

### Graph

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

### List

```bash
$ ansible-inventory -i inventory.yml --list
{
    "_meta": {
        "hostvars": {
            "sandbox-iosxe-latest-1.cisco.com": {
                "ansible_connection": "ansible.netcommon.network_cli",
                "ansible_network_os": "cisco.ios.ios",
                "ansible_password": "C1sco12345",
                "ansible_port": "22",
                "ansible_user": "developer"
            },
            "sandbox-iosxr-1.cisco.com": {
                "ansible_connection": "ansible.netcommon.network_cli",
                "ansible_network_os": "cisco.iosxr.iosxr",
                "ansible_password": "C1sco12345",
                "ansible_port": "22",
                "ansible_user": "admin"
            },
            "sandbox-nxos-1.cisco.com": {
                "ansible_connection": "ansible.netcommon.httpapi",
                "ansible_httpapi_use_ssl": "yes",
                "ansible_httpapi_validate_certs": "no",
                "ansible_network_os": "cisco.nxos.nxos",
                "ansible_password": "Admin_1234!",
                "ansible_port": "443",
                "ansible_user": "admin"
            }
        }
    },
    "all": {
        "children": [
            "routers",
            "ungrouped"
        ]
    },
    "ios": {
        "hosts": [
            "sandbox-iosxe-latest-1.cisco.com"
        ]
    },
    "iosxr": {
        "hosts": [
            "sandbox-iosxr-1.cisco.com"
        ]
    },
    "nxos": {
        "hosts": [
            "sandbox-nxos-1.cisco.com"
        ]
    },
    "routers": {
        "children": [
            "ios",
            "iosxr",
            "nxos"
        ]
    }
}
```