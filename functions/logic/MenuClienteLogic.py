import time
from functions.Generic_functions.MostrarCompras import MostrarCompras
from functions.Generic_functions.clear import clear
from functions.menus.ClientLoginScreen import ClientLoginScreen
from functions.menus.MenuCliente import MenuCliente
from functions.menus.MenuCompras import MenuCompras


def MenuClientelogic():
    cpf , validation = ClientLoginScreen()
    cpf1 = "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
    if not validation:
        clear()
        print (f"\t\t\tO CPF:{cpf1} não esta cadastrado ou a senha esta incorreta...")
        time.sleep(3)
        return
    iniciar = True
    while iniciar == True:
        option = MenuCliente()
        if option == 1:
            MenuCompras(cpf)
        elif option == 2:
            MostrarCompras(cpf)
        elif option == 0:
            iniciar == False