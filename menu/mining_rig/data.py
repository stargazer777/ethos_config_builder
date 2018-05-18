
def list_rigs():
    import mysql_ethos_manager.mining_rig
    import menu.display
    rows = mysql_ethos_manager.mining_rig.get_all_rig_names()
    menu.display.clear_screen()
    print "This is a list of the mining rigs."
    for row in rows:
        print " " * 2 + row[0]
    raw_input("Press Enter to Continue ...")
    return 0

def select_rig():
    import mysql_ethos_manager.mining_rig
    import menu.display
    rows = mysql_ethos_manager.mining_rig.get_all()
    menu.display.clear_screen()
    print "Select one of the mining rigs."
    for row in rows:
        print str(row[0]) + " -- " + row[1]
    return 0

def add_rig():
    import menu.display
    import mysql_ethos_manager.mining_rig
    import menu.mining_site.data
    menu.display.clear_screen()
    mining_rig_name = menu.display.text_line('Name of new mining rig: ')
    reboot_value = menu.display.text_line('Starting reboot value [0]: ', 0)
    ethos_ver_id = 0
    # Lookup mining_site_id
    menu.mining_site.data.select_site()
    mining_site_id = menu.display.select_int()
    mysql_ethos_manager.mining_rig.set_new_rig(mining_rig_name, reboot_value, ethos_ver_id, mining_site_id)
    return 0


def delete_rig():
    import mysql_ethos_manager.mining_rig
    import menu.display
    select_rig()
    mining_rig_id = menu.display.select_int()
    rows_deleted = mysql_ethos_manager.mining_rig.delete_rig(mining_rig_id)
    print str(rows_deleted) + " rig Deleted"
    raw_input("Press Enter to Continue ...")
    return 0




