## Inventory plugin demo

```bash
$ ansible-inventory -i inventory.yml --graph
@all:
  |--@ios:
  |  |--sandbox-iosxe-latest-1.cisco.com
  |--@iosxr:
  |  |--sandbox-iosxr-1.cisco.com
  |--@nxos:
  |  |--sandbox-nxos-1.cisco.com
  |--@ungrouped:
```

```bash
$ ansible-inventory -i inventory.yml --list
{
    "_meta": {
        "hostvars": {
            "sandbox-iosxe-latest-1.cisco.com": {
                "connection": "ansible.netcommon.network_cli",
                "network_os": "cisco.ios.ios",
                "password": "C1sco12345",
                "port": "22",
                "user": "developer"
            },
            "sandbox-iosxr-1.cisco.com": {
                "connection": "ansible.netcommon.network_cli",
                "network_os": "cisco.iosxr.iosxr",
                "password": "C1sco12345",
                "port": "22",
                "user": "admin"
            },
            "sandbox-nxos-1.cisco.com": {
                "connection": "ansible.netcommon.httpapi",
                "httpapi_use_ssl": "yes",
                "httpapi_validate_certs": "no",
                "network_os": "cisco.nxos.nxos",
                "password": "Admin_1234!",
                "port": "443",
                "user": "admin"
            }
        }
    },
    "all": {
        "children": [
            "ios",
            "iosxr",
            "nxos",
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
    }
}
```