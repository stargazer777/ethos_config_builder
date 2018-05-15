# This is the file to keep all the class data storage objects.

class payout_histroy:
    """" This class is to be used to store Algo data_storage before storing it into the database """

    def __init__(self):
        self.act_last24h = None
        self.algo_id = None
        self.algo_name = None
        self.est_current = None
        self.est_last24h = None
        self.pool_api_request_id = None
        self.pool_fee = None
        self.pool_mining_site_id = None
        self.pool_mining_url = None
        self.pool_mining_port = None
        self.pool_api_url = None
        self.pool_value_multi = 1000000
        self.pool_website_id = None
        self.pool_website_name = None
        self.pool_api_suffix = None

    def set_zpool_api_v(self, act_last24h, algo_name, est_current, est_last_24h, pool_fee, pool_mining_port,
                        pool_website_name, pool_api_request_id):
        self.pool_api_suffix = ""
        self.act_last24h = act_last24h
        self.algo_name = algo_name
        self.est_current = est_current
        self.est_last24h = est_last_24h
        self.pool_fee = pool_fee
        self.pool_mining_port = pool_mining_port
        self.pool_website_name = pool_website_name
        self.pool_api_request_id = pool_api_request_id
        self.set_algo_id()
        self.set_website_id()
        self.set_zpool_mining_url()
        self.set_mining_pool_site_id()

    def set_algo_id(self):
        import mysql_ethos_manager.algo
        if self.algo_name == None:
            print "no algo name has been set for this object"
        else:
            # get algo_id
            try:
                algo_id = mysql_ethos_manager.algo.get_id_by_name(self.algo_name)
                self.algo_id = algo_id
            except:
                print "Missing algo_id for : " + self.algo_name
                print "Adding Missing Algo  - " + self.algo_name
                try:
                    algo_id = mysql_ethos_manager.algo.put_new_algo(self.algo_name)
                    self.algo_id = algo_id
                except:
                    print "Adding Missing Algo Failed"

    def set_website_id(self):
        import mysql_ethos_manager.pool_website
        # get pool_website_id
        try:
            pool_website_id = mysql_ethos_manager.pool_website.get_id_by_name(self.pool_website_name)
        except:
            print "Unable to find website id - " + self.pool_website_name
        self.pool_website_id = pool_website_id

    def set_mining_pool_site_id(self):
        import mysql_ethos_manager.pool_mining_site as pms
        try:
            pool_mining_site_id = pms.get_id_by_website_id_and_algo_id(self.pool_website_id, self.algo_id)
        except:
            # Insert
            pool_mining_site_id = pms.insert(self.pool_website_id, self.algo_id, self.pool_mining_url,
                                             self.pool_mining_port, self.pool_api_suffix, self.pool_value_multi)
        self.pool_mining_site_id= pool_mining_site_id

    def set_api_url(self):
        import pool_website
        self.pool_api_url = pool_website.get_api_url_by_name(website_name)

    def set_zpool_mining_url(self):
        import mysql_ethos_manager.pool_website
        self.pool_mining_url = self.algo_name + "." + mysql_ethos_manager.pool_website.get_mining_url_by_name(self.pool_website_name)

    def save(self):
        import mysql_ethos_manager.mining_site_payout_history
        # insert into mysql - mining_site_payout_history
        try:
            rows_inserted = mysql_ethos_manager.mining_site_payout_history.insert(self.pool_api_request_id,
                                                                                  self.algo_id,
                                                                                  self.pool_mining_site_id,
                                                                                  self.pool_fee, self.est_current,
                                                                                  self.est_last24h,
                                                                                  self.act_last24h)
        except:
            print "Insert failed for mining_site_payout_history "
        return rows_inserted




