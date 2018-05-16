#This module is to interact with the MySQL Table mining site
import data_storage.mysql

def get_all():
    """returns tuple"""
    sql_str = "SELECT mining_site_id, mining_site_name FROM mining_site ORDER BY mining_site_name;"
    all_sites_tuple = data_storage.mysql.return_array(sql_str)
    return all_sites_tuple

def get_all_site_names():
    """returns tuple"""
    sql_str = "SELECT mining_site_name FROM mining_site ORDER BY mining_site_name;"
    all_sites_tuple = data_storage.mysql.return_array(sql_str)
    return all_sites_tuple

def set_new_site(mining_site_name):
    """returns int"""
    sql_str = "INSERT INTO mining_site (mining_site_name) VALUES ( '" + mining_site_name + "');"
    site_id = data_storage.mysql.insert_get_id(sql_str)
    return site_id

def delete_site(mining_site_id):
    """returns int"""
    sql_str = "DELETE from mining_site WHERE mining_site_id = " + str(mining_site_id) + ";"
    rows_deleted = data_storage.mysql.delete_row(sql_str)
    return rows_deleted
