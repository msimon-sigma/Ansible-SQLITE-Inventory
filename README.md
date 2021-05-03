# Ansible-SQLITE-Inventory
SQLITE as datasource inventory for Ansible

## Minimum requirements in DB :

- Table hosts : 

  columns : *hostname*, *groupname*
  
  ( rest of cols will be set as host_vars )
  
  
- Table groups :

  colums : *groupname*, *children_of*
  
  ( rest of cols will be set as group_vars )
  
  
- Complexe vars :

  colums : *hostname*
  
  use "table_host_vars" to set label of table to query, matches with be set as hostvar
   
  Example with var from table *inputs.disk*

## Script output :

```
{
    "_meta": {
        "hostvars": {
            "host1": {
                "ansible_port": "ansible_port1",
                "ansible_ssh_user": "ansible_ssh_user1",
                "groupname": "",
                "hostname": "host1",
                "inputs.disk": {
                    "ignore_fs": "['tmpfs', 'iso9660', 'overlay', 'aufs', 'squashfs']",
                    "mount_points": "['/']"
                }
            }
        }
    },
    "all": {
        "hosts": [
            "host1"
        ]
    },
    "group1": {
        "children": [],
        "hosts": [],
        "vars": {
            "children_of": "",
            "group_ansible_port": "ansible_port",
            "group_ansible_ssh_user": "11111ansible_ssh_user",
            "groupname": "group1"
        }
    }
}
```

## ansible-inventory --list

```
{
    "_meta": {
        "hostvars": {
            "host1": {
                "ansible_port": "ansible_port1",
                "ansible_ssh_user": "ansible_ssh_user1",
                "groupname": "",
                "hostname": "host1",
                "inputs.disk": {
                    "ignore_fs": "['tmpfs', 'iso9660', 'overlay', 'aufs', 'squashfs']",
                    "mount_points": "['/']"
                }
            }
        }
    },
    "all": {
        "children": [
            "group1",
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "host1"
        ]
    }
}
```


