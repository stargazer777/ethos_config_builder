

def sub_menu():
    import data
    import menu.display
    menu.display.clear_screen()
    menu_value = 0
    """This is the class for mining site"""
    print "Please select one of the following items you would like to run."
    print '-' * 10
    print "1 - List Sites"
    print "2 - Add Site"
    print "3 - Remove Site"
    print '-' * 10
    print "0 - Go Back."
    print '=' * 10

    menu_value = menu.display.select_int()

    # Process Menu Selection
    if menu_value == 0:
        return 0
    elif menu_value == 1:
        data.list_sites()
    elif menu_value == 2:
        data.add_site()
    elif menu_value == 3:
        data.delete_site()
    else:
        last_value = str(menu_value)
        print "  " + last_value + " is not an available option."
        raw_input("Press Enter to Continue ...")
    sub_menu()
