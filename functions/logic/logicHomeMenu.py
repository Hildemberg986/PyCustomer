from functions.Generic_functions.clear import clear
from functions.logic.logicCustomerMenu import logicCustomerMenu
from functions.menus.homemenu import homeMenu
import time


def logichomeMenu():
    print("dentro")
    iniciar = True
    while iniciar == True:
        option = homeMenu()
        if option == 1:
            logicCustomerMenu()
        elif option == 2:
            print ("2")
        elif option == 3:
            print("3")
        elif option == 0:
            clear()
            print("\t\t\t Programa encerrado")
            iniciar = False
        else:
            clear()
            print("\t\t\t Opção invalida...")
            time.sleep(2)