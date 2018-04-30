#This module is to interact with the MySQL Table pool_website
import database.mysql

def get_id_by_name(pool_name):
    sql_str = "SELECT pool_website_id FROM pool_website WHERE pool_name = '" + pool_name + "';"

    #Build database connection
    data = database.mysql.return_row(sql_str)
    pool_website_id = data[0]
    return pool_website_id

