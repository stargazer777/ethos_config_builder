#This module is to interact with the MySQL Table pool_mining_site
import database.mysql

def get_id_by_website_id_and_algo_id(pool_website_id, algo_id):
    sql_str = "SELECT pool_mining_site_id FROM pool_mining_site WHERE pool_website_id = " + str(pool_website_id) + " "
    sql_str += " AND algo_id = " + str(algo_id) + ";"

    #Build database connection
    data = database.mysql.return_row(sql_str)
    pool_mining_site_id = data[0]
    return pool_mining_site_id
