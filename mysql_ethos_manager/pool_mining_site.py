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
    sql_str = "INSERT INTO pool_mining_site (pool_website_id, algo_id, pool_mining_url, pool_mining_port, pool_suffix, "
    sql_str += "pool_value_mult) "
    sql_str += "Values (" + str(pool_website_id) + "," + str(algo_id) + ",'" + pool_mining_url + "'," + str(pool_mining_port)
    sql_str += ",'" + pool_api_suffix + "'," + str(pool_value_mult) + ");"
    rows_inserted = data_storage.mysql.insert(sql_str)
    return rows_inserted

def insert_zpool(algo_name):
    website_name = "zpool"
    pool_api_suffix = ""
    pool_value_multi = 1000000
    import pool_website

    #build_mining_url
    pool_mining_url = algo_name + "." + pool_website.get_mining_url_by_name(website_name)

    #get api_url
    api_url = pool_website.get_api_url_by_name(website_name)

    #get data_storage from api
    #todo you need to sleep
    # time.sleep()
    return 0
    has_unicode = True
    api_data = poll_remote_api.json_api.poll_json(api_url, has_unicode)
    for algo in api_data:
        algo_api_name = api_data[algo]['name']
        if algo_name == algo_api_name:
            algo_port = api_data[algo]['port']
            insert(pool_website_id, algo_id, pool_mining_url, algo_port, pool_api_suffix, pool_value_multi)
            return 0
        else:
            return 1




