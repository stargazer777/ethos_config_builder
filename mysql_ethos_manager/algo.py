#This module is to interact with the MySQL Table algo

def get_id_by_name(algo_name):
    sql_str = "SELECT algo_id FROM algo WHERE algo_name = '" + algo_name + "';"

    #Build data_storage connection
    data = data.mysql.return_row(sql_str)
    algo_id = data[0]
    return algo_id
