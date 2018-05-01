#This module is to interact with the MySQL Table pool_website
import data_storage.mysql

def get_id_by_name(pool_name):
    sql_str = "SELECT pool_website_id FROM pool_website WHERE pool_name = '" + pool_name + "';"

    #Build data_storage connection
    data = data_storage.mysql.return_row(sql_str)
    pool_website_id = data[0]
    return pool_website_id

def get_mining_url_by_name(pool_name):
    sql_str = "SELECT pool_url FROM pool_website WHERE pool_name = '" + pool_name + "';"

    #Build data_storage connection
    data = data_storage.mysql.return_row(sql_str)
    pool_mining_url = data[0]
    return pool_mining_url

def get_api_url_by_name(pool_name):
    sql_str = "SELECT pool_api_url FROM pool_website WHERE pool_name = '" + pool_name + "';"

    #Build data_storage connection
    data = data_storage.mysql.return_row(sql_str)
    pool_api_url = data[0]
    return pool_api_url
