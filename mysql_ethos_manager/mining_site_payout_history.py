#This module is to interact with the MySQL Table mining_site_payout_histoty

import database.mysql
import algo
import pool_mining_site


def insert(pool_website_id, pool_api_request_id, algo_name, algo_fee, algo_est_cur, algo_est_last24, algo_act_last24 ):
    rows_inserted = 0

    # get alg id
    try:
        algo_id = algo.get_id_by_name(algo_name)
    except:
        print "Error Looking up algo: " + algo_name
        return 0

    #get pool_mining_site_id
    try:
        pool_mining_site_id = pool_mining_site.get_id_by_website_id_and_algo_id(pool_website_id, algo_id)
    except:
        print "Error Looking up pool_mining_site_id  algo_id: " + str(algo_id) + " pool_website_id: " + str(pool_website_id)
        return 0


    print "Debuging"
    print "pool_website_id:" +str(pool_website_id)
    print "pool_api_request_id: " + str(pool_api_request_id)
    print "alg_id: " + str(algo_id)
    print ""

    sql_str = "INSERT into mining_site_payout_history "
    sql_str += "(pool_api_request_id, algo_id, pool_mining_site_id, pool_fee, est_current, est_last24h, act_last24h) "
    sql_str += "VALUES (" + str(pool_api_request_id) + "," + str(algo_id) + "," + str(pool_mining_site_id) + ","
    sql_str += str(algo_fee) + "," + str(algo_est_cur) + "," + str(algo_est_last24) + "," + str(algo_act_last24)+ ");"

    # Build database connection
    print sql_str
    rows_inserted = database.mysql.insert(sql_str)
    return rows_inserted
