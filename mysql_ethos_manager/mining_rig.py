#This module is to interact with the MySQL Table mining rig
import data_storage.mysql

def get_all():
    """returns tuple"""
    sql_str = "SELECT mining_rig_id, mining_rig_name, reboot_value, ethos_ver_id, mining_site_id, mining_rig_uuid "
    sql_str += "FROM mining_rig ORDER BY mining_rig_name;"
    all_rigs_tuple = data_storage.mysql.return_array(sql_str)
    return all_rigs_tuple

def get_all_rig_names():
    """returns tuple"""
    sql_str = "SELECT mining_rig_name FROM mining_rig ORDER BY mining_rig_name;"
    all_rigs_tuple = data_storage.mysql.return_array(sql_str)
    return all_rigs_tuple

def set_new_rig(mining_rig_name, reboot_value, ethos_ver_id, mining_site_id):
    """returns int"""
    mining_rig_uuid = 'UUID()'
    sql_str = "INSERT INTO mining_rig (mining_rig_name, reboot_value, ethos_ver_id, mining_site_id, "
    sql_str += "mining_rig_uuid) VALUES ( '" + mining_rig_name + "', " + str(reboot_value) + ", "
    sql_str += str(ethos_ver_id) + ", " + str(mining_site_id) + "," + mining_rig_uuid + ");"
    rig_id = data_storage.mysql.insert_get_id(sql_str)
    return rig_id

def delete_rig(mining_rig_id):
    """returns int"""
    sql_str = "DELETE from mining_rig WHERE mining_rig_id = " + str(mining_rig_id) + ";"
    rows_deleted = data_storage.mysql.delete_row(sql_str)
    return rows_deleted
