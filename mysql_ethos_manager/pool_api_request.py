#This module is to interact with the MySQL Table pool_api_requesst
import data_storage.mysql


def get_new_id(pool_website_id):
    sql_str = "INSERT into pool_api_request (pool_website_id, pool_api_timestamp) "
    sql_str += "VALUES (" + str(pool_website_id) + ", now());"
    # Build data_storage connection

    last_row_id = data_storage.mysql.insert_get_id(sql_str)
    return last_row_id




