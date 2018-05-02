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
        self.pool_mining_port = None
        self.pool_value_multi = 1000000
        self.pool_website_id = None
        self.pool_website_name = None

    def set_zpool_api_v(self, act_last24h, algo_name, est_current, est_last_24h, pool_fee, pool_mining_port,
                        pool_website_name, pool_api_request_id):
        self.act_last24h = act_last24h
        self.algo_name = algo_name
        self.est_current = est_current
        self.est_last24h = est_last_24h
        self.pool_fee = pool_fee
        self.pool_mining_port = pool_mining_port
        self.pool_website_name = pool_website_name
        self.pool_api_request_id = pool_api_request_id
        #
        # self.set_algo_id(algo_name)
        # self.set_website_id(pool_website_name)

    def set_algo_id(self,loop_id=0):
        import mysql_ethos_manager.algo
        if self.algo_name == None:
            print "no algo name has been set for this object"
        else:
            # get algo_id
            try:
                algo_id = mysql_ethos_manager.algo.get_id_by_name(self.algo_name)
                self.algo_id = algo_id
            except:
                print "Missing algo_id for  : " + self.algo_name
                #todo add missing algo id and try again.
                if loop_id == 0:
                    loop_id += 1
                    self.set_algo_id(loop_id)
                else:
                    return 1

    def set_website_id(self, website_name):
        import mysql_ethos_manager.pool_website
        # get pool_website_id
        pool_website_id = mysql_ethos_manager.pool_website.get_id_by_name(website_name)
        if type(pool_website_id) == int:
            self.pool_website_id = pool_website_id

    def get_mining_url(self, website_name, algo_name):
        import mysql_ethos_manager.pool_website
        self.pool_mining_url = algo_name + "." + mysql_ethos_manager.pool_website.get_mining_url_by_name(website_name)


    def save(self, database):
        # insert into mysql - mining_site_payout_history
        rows_inserted = mysql_ethos_manager.mining_site_payout_history.insert(pool_api_request_id,
                                                                             self.pool_api_request_id,
                                                                             self.pool_mining_site_id, pool_fee,
                                                                             est_current, est_last_24h, act_last24h)
        return rows_inserted




