# This is used to help with common display issues.


def clear_screen():
    import platform
    import os
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    return()


def select_int():
    is_valid = 0
    while not is_valid:
        try:
            menu_value = int(raw_input('Select ID : '))
            is_valid = 1
        except :
            print "That is not a number.\n"
            raw_input("Press Enter to Continue ...")
    return menu_value


def text_line(title, value_default=None):
    try:
        menu_value = raw_input(title) or value_default
    except:
        print "Invaild Name. \n"
        raw_input("Press Enter to Continue ...")
    return menu_value
