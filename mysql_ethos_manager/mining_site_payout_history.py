# This module is to interact with the MySQL Table mining_site_payout_histoty
import data_storage.mysql

def insert(pool_api_request_id, algo_id, pool_mining_site_id, algo_fee, algo_est_cur, algo_est_last24, algo_act_last24 ):
    rows_inserted = 0

    sql_str = "INSERT into mining_site_payout_history "
    sql_str += "(pool_api_request_id, algo_id, pool_mining_site_id, pool_fee, est_current, est_last24h, act_last24h) "
    sql_str += "VALUES (" + str(pool_api_request_id) + "," + str(algo_id) + "," + str(pool_mining_site_id) + ","
    sql_str += str(algo_fee) + "," + str(algo_est_cur) + "," + str(algo_est_last24) + "," + str(algo_act_last24)+ ");"

    # Build data_storage connection
    rows_inserted = data_storage.mysql.insert(sql_str)
    return rows_inserted
