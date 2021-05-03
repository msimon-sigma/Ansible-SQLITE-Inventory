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
  


'''
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

'''


