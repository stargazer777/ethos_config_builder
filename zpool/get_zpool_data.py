def start_poll():
    # run this poller to import zpool.ca data_storage.
    import poll_remote_api.json_api
    import data_storage.data_store
    import mysql_ethos_manager.pool_website
    import mysql_ethos_manager.pool_api_request
    import mysql_ethos_manager.mining_site_payout_history

    pool_name = "zpool"
    pool_url = "zpool.ca"
    pool_api_url = "zpool.ca/api/status"
    has_unicode = True
    DEBUG = True

    # get pool_website_id
    try:
        pool_website_id = mysql_ethos_manager.pool_website.get_id_by_name(pool_name)
    except:
        print "Error looking up pool_website_id"
        print "Adding " + pool_name +  " to pool_website table"
        try:
            pool_website_id = mysql_ethos_manager.pool_website.get_new_pool_website(pool_name, pool_url, pool_api_url)
        except:
            print "Pool Website insert failed. "
            exit(1)

    # get pool_api_request_id
    try:
        pool_api_request_id = mysql_ethos_manager.pool_api_request.get_new_id(pool_website_id)
    except:
        print "Error getting new api_request_id"
        exit(1)

    full_api_url = "http://www." + pool_api_url
    print full_api_url
    api_data = poll_remote_api.json_api.poll_json(full_api_url, has_unicode)
    # pprint.pprint(api_data)

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
        algo_obj.set_zpool_api_v(algo_act_last24, algo_name, algo_est_cur, algo_est_last24, algo_fee, algo_port,
                                 pool_name, pool_api_request_id)

        rows_added += algo_obj.save()
        algo_dict[algo_name] = algo_obj

    return(rows_added)

    # pprint.pprint(algo_dict)
    # print "-----"
    # pprint.pprint(algo_dict["c11"].pool_fee)
