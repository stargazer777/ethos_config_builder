
def main_menu():
    menu_value = None
    """This is the class for the main menu"""
    print "Please select one of the following items you would like to run."
    print '-' * 10
    print "1 - Mining Sites"
    print "2 - Mining Rigs"
    print "3 - Current Pool Profit Report"
    print '-' * 10
    print "0 - Exit"
    print '=' * 10

    is_valid = 0
    while not is_valid:
        try:
            menu_value = int(raw_input('Select Option: '))
            is_valid = 1
        except :
            print "That is not a number.\n"
            main_menu()

    # Process Menu Selection
    if menu_value == 0:
        exit(0)
    if menu_value == 1:
        import menu.mining_site.sub_menu
        menu.mining_site.sub_menu.sub_menu()
        main_menu()
    if menu_value == 2:
        print "Yea " + str(menu_value)

    else:
        print "  " + str(menu_value) + " is not an available option."
        main_menu()

    print menu_value
