#This module is to interact with the MySQL Table pool_mining_site
import data_storage.mysql


def get_id_by_website_id_and_algo_id(pool_website_id, algo_id):
    sql_str = "SELECT pool_mining_site_id FROM pool_mining_site WHERE pool_website_id = " + str(pool_website_id) + " "
    sql_str += " AND algo_id = " + str(algo_id) + ";"

    #Build data_storage connection
    data = data.mysql.return_row(sql_str)
    pool_mining_site_id = data[0]
    return pool_mining_site_id

def insert(pool_website_id, algo_id, pool_mining_url, pool_mining_port, pool_api_suffix, pool_value_mult):
    sql_str = "INSERT INTO pool_mining_site (pool_website_id, pool_mining_algo_id, pool_mining_url, pool_mining_port, "
    sql_str += "pool_api_suffix, pool_value_mult) "
    sql_str += "Values (" + str(pool_website_id) + "," + str(algo_id) + ",'" + pool_mining_url + "'," + str(pool_mining_port)
    sql_str += ",'" + pool_api_suffix + "'," + str(pool_value_mult) + ");"
    rows_inserted = data_storage.mysql.insert(sql_str)
    return rows_inserted




