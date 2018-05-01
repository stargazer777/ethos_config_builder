class payout_histroy:
    """" This class is to be used to store Algo data_storage before storing it into the database """
    act_last24h = None
    algo_id = None
    algo_name = None
    est_current = None
    est_last24h = None
    pool_api_request_id = None
    pool_fee = None
    pool_mining_site_id = None
    pool_mining_url = None
    pool_value_multi = 1000000
    pool_website_id = None
    pool_website_name = None

    def __init__(self, act_last24h, algo_id, algo_name, est_current, est_last24h, pool_api_request_id, pool_fee,
                 pool_mining_site_id, pool_mining_url, pool_value_multi,  pool_website_id, pool_website_name):
        self.act_last24h = act_last24h
        self.algo_id = algo_id
        self.algo_name = algo_name
        self.est_current = est_current
        self.est_last24h = est_last24h
        self.pool_api_request_id = pool_api_request_id
        self.pool_fee = pool_fee
        self.pool_mining_site_id = pool_mining_site_id
        self.pool_mining_url = pool_mining_url
        self.pool_value_multi = pool_value_multi
        self.pool_website_id = pool_website_id
        self.pool_website_name = pool_website_name

    def set_algo(self, algo_name):
        import mysql_ethos_manager.algo
        self.algo_name = algo_name
        # get algo_id
        algo_id = mysql_ethos_manager.algo.get_id_by_name(algo_name)
        if type(algo_id) == int:
            self.algo_id = algo_id

    def set_website(self, website_name):
        import mysql_ethos_manager.pool_website
        # get pool_website_id
        pool_website_id = mysql_ethos_manager.pool_website.get_id_by_name(website_name)
        if type(pool_website_id) == int:
            self.pool_website_id = pool_website_id

    def set_mining_url(self, website_name, algo_name):
        import mysql_ethos_manager.pool_website
        self.pool_mining_url = algo_name + "." + mysql_ethos_manager.pool_website.get_mining_url_by_name(website_name)






