# run this poller to import zpool.ca data.
import sys
import poll_remote_api.json_api
import mysql_ethos_manager.mining_site_payout_history
import pprint

url = "https://www.zpool.ca/api/status"
has_unicode = True
DEBUG = True
website = "zpool.ca"

api_data = poll_remote_api.json_api.poll_json(url, has_unicode)
# pprint.pprint(api_data)
rows_added = 0
for algo in api_data:
    algo_name = api_data[algo]['name']
    algo_port = api_data[algo]['port']
    algo_fee = api_data[algo]['fees']
    algo_est_cur = api_data[algo]['estimate_current']
    algo_est_last24 = api_data[algo]['estimate_last24h']
    algo_act_last24 = api_data[algo]['actual_last24h']
    save_data = mysql_ethos_manager.mining_site_payout_history.insert(website,algo_name, algo_fee, algo_est_cur, algo_est_last24, algo_act_last24)
    rows_added += int(save_data)

if int(rows_added) == 0:
    sys.exit(1)
else:
    print "records inserted: " + str(rows_added)
    sys_exit(0)