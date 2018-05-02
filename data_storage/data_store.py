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
                        pool_website_name):
        self.act_last24h = act_last24h
        self.algo_name = algo_name
        self.est_current = est_current
        self.est_last24h = est_last_24h
        self.pool_fee = pool_fee
        self.pool_mining_port = pool_mining_port
        self.pool_website_name = pool_website_name
        # self.set_algo_id(algo_name)
        # self.set_website_id(pool_website_name)

    def set_algo_id(self, algo_name):
        import mysql_ethos_manager.algo
        self.algo_name = algo_name
        # get algo_id
        algo_id = mysql_ethos_manager.algo.get_id_by_name(algo_name)
        if type(algo_id) == int:
            self.algo_id = algo_id

    def set_website_id(self, website_name):
        import mysql_ethos_manager.pool_website
        # get pool_website_id
        pool_website_id = mysql_ethos_manager.pool_website.get_id_by_name(website_name)
        if type(pool_website_id) == int:
            self.pool_website_id = pool_website_id

    def get_mining_url(self, website_name, algo_name):
        import mysql_ethos_manager.pool_website
        self.pool_mining_url = algo_name + "." + mysql_ethos_manager.pool_website.get_mining_url_by_name(website_name)






