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

### Using the inventory

```json
$ ansible routers -i inventory.yml -m ping
sandbox-iosxr-1.cisco.com | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
sandbox-nxos-1.cisco.com | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
sandbox-iosxe-latest-1.cisco.com | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

```bash
$ ansible ios -i inventory.yml -m ansible.netcommon.cli_command -a "command='show version'"
sandbox-iosxe-latest-1.cisco.com | SUCCESS => {
    "changed": false,
    "stdout": "Cisco IOS XE Software, Version 17.03.01a\nCisco IOS Software [Amsterdam], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 17.3.1a, RELEASE SOFTWARE (fc3)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2020 by Cisco Systems, Inc.\nCompiled Wed 12-Aug-20 00:16 by mcpre\n\n\nCisco IOS-XE software, Copyright (c) 2005-2020 \n\nConfiguration register is 0x2102",
    "stdout_lines": [
        "Cisco IOS XE Software, Version 17.03.01a",
        "software.",
        "",
        "",
        "ROM: IOS-XE ROMMON",
        "csr1000v-1 uptime is 3 days, 6 hours, 21 minutes",
        "Uptime for this control processor is 3 days, 6 hours, 23 minutes",
        "System returned to ROM by reload",
        "System image file is \"bootflash:packages.conf\"",
        "Last reload reason: reload",
        "",
        "",
        "",
        "This product contains cryptographic features and is subject to United",
        "States and local country laws governing import, export, transfer and",
        "use. Delivery of Cisco cryptographic products does
         ...
        "cisco CSR1000V (VXE) processor (revision VXE) with 715705K/3075K bytes of memory.",
        "Processor board ID 9ESGOBARV9D",
        "Router operating mode: Autonomous",
        "3 Gigabit Ethernet interfaces",
        "32768K bytes of non-volatile configuration memory.",
        "3978420K bytes of physical memory.",
        "6188032K bytes of virtual hard disk at bootflash:.",
        "",
        "Configuration register is 0x2102"
    ]
}
```