#!/usr/bin/python3.8
import os
import sys
import sqlite3

# Format Ansible expects for all
# { "group1": { "hosts": [], "vars": {} }, "group2": { "hosts": [], "vars": {} }, "_meta": {"hostvars": {}} }

def init_sample_if_empty(): 
    return

try:
    import json
except ImportError:
    import simplejson as json

def query_db(query):
    db_connection = sqlite3.connect("/vagrant/ansible/data.db")
    db_connection.row_factory = sqlite3.Row
    c = db_connection.cursor()
    c.execute(query)
    query_result = c.fetchall()
    db_connection.commit()
    db_connection.close()
    return query_result

def query_all_hosts():
    return [row[0] for row in query_db('SELECT hostname from hosts')]
def query_group_list():
    return [row[0] for row in query_db('SELECT groupname from groups')]
def query_group_host():
    return [row[0] for row in query_db('SELECT groupname from hosts')]
def query_members_of(groupname):
    return [ ix[0] for ix in query_db('SELECT hostname from hosts WHERE groupname = "'+groupname+ '"') ]
def query_children_of(groupname):
    return [ ix[0] for ix in query_db('SELECT groupname from groups WHERE children_of = "'+groupname+ '"') ]


    
def query_group_vars(groupname):
    result = [dict(ix) for ix in query_db('SELECT * from groups WHERE groupname = "'+groupname+ '"') ]
    try:
        return result[0]
    except:
        return {}
def query_host_args(hostname):
    vars_dict = {}
    query_result=query_db('SELECT * FROM hosts WHERE hostname = "' + hostname + '"')
    result = [dict(ix) for ix in query_result]
    try:
        return result[0]
    except:
        return {}

def main():
    init_sample_if_empty()
    inventory_dict = dict()
    inventory_dict['_meta'] = {}
    inventory_dict['_meta']['hostvars'] = {}
    unprocessed_hosts = query_all_hosts()
    # group in groups table and in host tables
    full_grouplist = list(dict.fromkeys(query_group_list() + query_group_host()))
    # build group bloc
    for groupname in full_grouplist:
        if groupname == '':
            continue
        inventory_dict[groupname] = {}
        inventory_dict[groupname]['hosts'] = query_members_of(groupname)
        inventory_dict[groupname]['vars'] = query_group_vars(groupname)
        inventory_dict[groupname]['children'] = query_children_of(groupname)
        # Append hostvars to _meta
        for hostname in query_members_of(groupname):
            inventory_dict['_meta']['hostvars'][hostname] = query_host_args(hostname)
            unprocessed_hosts.remove(hostname)
    # ungrouped
    for hostname in unprocessed_hosts :
        inventory_dict['_meta']['hostvars'][hostname] = query_host_args(hostname)
    inventory_dict['all'] = {}
    inventory_dict['all']['hosts']=query_all_hosts()
    print(json.dumps(inventory_dict, indent=4, sort_keys=True))
    sys.exit(0)

if __name__ == "__main__":
    main()
