## Inventory plugin demo

```bash
$ ansible-inventory -i inventory.yml --graph
@all:
  |--@ungrouped:
  |  |--sandbox-iosxe-latest-1.cisco.com
  |  |--sandbox-iosxr-1.cisco.com
  |  |--sandbox-nxos-1.cisco.com
```

```bash
$ ansible-inventory -i inventory.yml --list
{
    "_meta": {
        "hostvars": {
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
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "sandbox-iosxe-latest-1.cisco.com",
            "sandbox-iosxr-1.cisco.com",
            "sandbox-nxos-1.cisco.com"
        ]
    }
}
```