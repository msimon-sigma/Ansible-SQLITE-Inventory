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
  
