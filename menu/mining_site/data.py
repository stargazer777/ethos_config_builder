
def list_sites():
    import mysql_ethos_manager.mining_site
    import menu.display
    rows = mysql_ethos_manager.mining_site.get_all_sites()
    menu.display.clear_screen()
    print "This is a list of the mining sites."
    for row in rows:
        print " " * 2 + row[0]
    raw_input("Press Enter to Continue ...")
    return 0

def add_site(mining_site_name):
    import mysql_ethos_manager.mining_site
    mysql_ethos_manager.mining_site.set_new_site(mining_site_name)
    return 0


