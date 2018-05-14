#This module is to interact with the MySQL Table algo
import data_storage.mysql

def get_id_by_name(algo_name):
    sql_str = "SELECT algo_id FROM algo WHERE algo_name = '" + algo_name + "';"

    #Build data_storage connection
    data = data_storage.mysql.return_row(sql_str)
    algo_id = data[0]
    return algo_id

def put_new_algo(algo_name):
    sql_str = "INSERT INTO algo (algo_name) VALUES ( '" + algo_name + "');"
    algo_id = data_storage.mysql.insert_get_id(sql_str)
    return algo_id