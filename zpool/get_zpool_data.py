# run this poller to import zpool.ca data_storage.
import poll_remote_api.json_api
import mysql_ethos_manager.pool_website
import mysql_ethos_manager.pool_api_request
import data_storage.data_store
import pprint

pool_name = "zpool"
url = "https://www.zpool.ca/api/status"
has_unicode = True
DEBUG = True

api_data = poll_remote_api.json_api.poll_json(url, has_unicode)
# pprint.pprint(api_data)

# get pool_website_id
try:
    pool_website_id = 1
    # pool_website_id = mysql_ethos_manager.pool_website.get_id_by_name(pool_name)
except:
    print "Error looking up pool_website_id"
    exit(1)

# get pool_api_request_id
try:
    pool_api_request_id = 1
    # pool_api_request_id = mysql_ethos_manager.pool_api_request.get_new_id(pool_website_id)
except:
    print "Error getting new api_request_id"
    exit(1)

rows_added = 0
algo_dict = {}
for algo in api_data:
    algo_obj = data_storage.data_store.payout_histroy()
    algo_name = api_data[algo]['name']
    algo_port = api_data[algo]['port']
    algo_fee = api_data[algo]['fees']
    algo_est_cur = api_data[algo]['estimate_current']
    algo_est_last24 = api_data[algo]['estimate_last24h']
    algo_act_last24 = api_data[algo]['actual_last24h']

    #write to object
    algo_obj.set_zpool_api_v(algo_act_last24, algo_name, algo_est_cur, algo_est_last24, algo_fee, algo_port, pool_name)
    algo_dict[algo_name] = algo_obj

# pprint.pprint(algo_dict)
# print "-----"
# pprint.pprint(algo_dict["c11"].pool_fee)

#    save_data = mysql_ethos_manager.mining_site_payout_history.insert(pool_website_id, pool_api_request_id, algo_name, algo_fee, algo_est_cur, algo_est_last24, algo_act_last24)
#    if type(save_data) is int:
#        rows_added += int(save_data)
#    elif type(save_data) is str:
#        if save_data == "Missing_Site":
#            import mysql_ethos_manager.pool_mining_site
#            mysql_ethos_manager.pool_mining_site.insert_zpool(algo_name)
#            save_data = mysql_ethos_manager.mining_site_payout_history.insert(pool_website_id, pool_api_request_id, algo_name, algo_fee, algo_est_cur, algo_est_last24, algo_act_last24)
#            if save_data is int:
#                rows_added += int(save_data)
#                print "Added Algo " + algo_name + " to pool_mining_site"
#            else:
#                print "Failed to insert " + algo_name

#if int(rows_added) == 0:
#    sys.exit(1)
#else:
#    print "records inserted: " + str(rows_added)
#    sys.exit(0)