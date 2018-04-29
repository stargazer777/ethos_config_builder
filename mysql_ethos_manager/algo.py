#This module is to interact with the MySQL Table algo
import database.mysql

def get_id_by_name(algo_name):
    sql_str = "SELECT algo_id FROM algo WHERE algo_name = '" + algo_name + "';"

    #Build database connection
    data = database.mysql.return_row(sql_str)
    algo_id = data[0]
    return algo_id

algo  = get_id_by_name('x11')