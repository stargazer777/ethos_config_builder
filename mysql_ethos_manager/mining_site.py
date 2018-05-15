#This module is to interact with the MySQL Table mining site
import data_storage.mysql

def get_all_sites():
    sql_str = "SELECT mining_site_name FROM mining_site ORDER BY mining_site_name;"
    all_sites_array = data_storage.mysql.return_array(sql_str)
    return all_sites_array

def set_new_site(mining_site_name):
    sql_str = "INSERT INTO mining_site (mining_site_name) VALUES ( '" + mining_site_name + "');"
    site_id = data_storage.mysql.insert_get_id(sql_str)
    return site_id