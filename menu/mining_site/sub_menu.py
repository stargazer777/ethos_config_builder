def sub_menu():
    import data
    menu_value = 0
    """This is the class for mining site"""
    print "Please select one of the following items you would like to run."
    print '-' * 10
    print "1 - List Sites"
    print "2 - Add Sites"
    print "3 - Remove Sites"
    print '-' * 10
    print "0 - Go Back."
    print '=' * 10

    is_valid = 0
    while not is_valid:
        try:
            menu_value = int(raw_input('Select Option: '))
            is_valid = 1
        except :
            print "That is not a number.\n"
            sub_menu()

    # Process Menu Selection
    if menu_value == 0:
        return 0
    elif menu_value == 1:
        data.list_sites()
        sub_menu()
    elif menu_value == 2:
        try:
            mining_site_name = raw_input('Name of new site: ')
            data.add_site(mining_site_name)
        except:
            print "Invaild Name. \n"
            sub_menu()
    else:
        print "  " + str(menu_value) + " is not an available option."



    print menu_value