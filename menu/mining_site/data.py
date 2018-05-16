
def list_sites():
    import mysql_ethos_manager.mining_site
    import menu.display
    rows = mysql_ethos_manager.mining_site.get_all_site_names()
    menu.display.clear_screen()
    print "This is a list of the mining sites."
    for row in rows:
        print " " * 2 + row[0]
    raw_input("Press Enter to Continue ...")
    return 0

def select_site():
    import mysql_ethos_manager.mining_site
    import menu.display
    rows = mysql_ethos_manager.mining_site.get_all()
    menu.display.clear_screen()
    print "Select one of the mining sites."
    for row in rows:
        print str(row[0]) + " -- " + row[1]
    return 0

def add_site():
    import menu.display
    import mysql_ethos_manager.mining_site
    menu.display.clear_screen()
    try:
        mining_site_name = raw_input('Name of new site: ')
    except:
        print "Invaild Name. \n"
        raw_input("Press Enter to Continue ...")
        add_site()

    mysql_ethos_manager.mining_site.set_new_site(mining_site_name)
    return 0


def delete_site():
    import mysql_ethos_manager.mining_site
    import menu.display
    select_site()
    mining_site_id = menu.display.select_int()
    rows_deleted = mysql_ethos_manager.mining_site.delete_site(mining_site_id)
    print str(rows_deleted) + " Site Deleted"
    raw_input("Press Enter to Continue ...")
    return 0




