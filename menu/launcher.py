
def main_menu():
    import menu.display
    menu_value = None
    menu.display.clear_screen()
    """This is the class for the main menu"""
    print "Please select one of the following items you would like to run."
    print '-' * 10
    print "1 - Mining Sites"
    print "2 - Mining Rigs"
    print "3 - Current Pool Profit Report"
    print '-' * 10
    print "0 - Exit"
    print '=' * 10

    menu_value = menu.display.select_int()

    # Process Menu Selection
    if menu_value == 0:
        exit(0)
    if menu_value == 1:
        import menu.mining_site.sub_menu
        menu.mining_site.sub_menu.sub_menu()
        main_menu()
    else:
        print "  " + str(menu_value) + " is not an available option."
        raw_input("Press Enter to Continue ...")
        main_menu()

    print menu_value
