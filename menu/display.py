# This is used to help with common display issues.


def clear_screen():
    import platform
    import os
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    return()
