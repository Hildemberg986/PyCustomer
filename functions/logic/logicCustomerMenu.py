from functions.Generic_functions.clear import clear
from functions.logic.MenuClienteLogic import MenuClientelogic
from functions.menus.AdminLoginScreen import adminLoginScreen
from functions.menus.ClientLoginScreen import ClientLoginScreen
from functions.menus.ClientRegistrationScreen import ClientRegistrationScreen
from functions.menus.customermenu import customerMenu
import time


def logicCustomerMenu():
    iniciar = True
    while iniciar == True:
        option = customerMenu()
        if option == 1:
           adminLoginScreen()
        elif option == 2:
            MenuClientelogic()
        elif option == 3:
            ClientRegistrationScreen()
        elif option == 0:
            iniciar = False
        else:
            clear()
            print("\t\t\t Opção invalida...")
            time.sleep(2)