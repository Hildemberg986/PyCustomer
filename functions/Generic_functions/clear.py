#função para limpar console
def clear():
    import os
    import platform
    desk = platform.system()
    if desk == 'Windows':
        os.system('cls')
    else:
        os.system('clear')