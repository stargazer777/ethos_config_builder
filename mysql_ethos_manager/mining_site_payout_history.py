#This module is to interact with the MySQL Table mining_site_payout_histoty

import database.mysql
import algo

def insert(pool_name, algo_name, algo_fee, algo_est_cur, algo_est_last24, algo_act_last24 ):
    rows_inserted = 0

    #get alg id
    try:
        algo_id = algo.get_id_by_name(algo_name)
    except:
        print "Error Looking up algo: " + algo_name
        return 0






    return rows_inserted
