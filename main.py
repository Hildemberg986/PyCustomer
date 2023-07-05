from functions.create.createuser import *
from functions.search import *
from functions.delete import *
from functions.clear import *
from functions.datebase import *
from functions.validations.checkerCPF import *
from functions.upgradeuser import *
from functions.menus.customermenu import *
from functions.menus.homemenu import *
from functions.menus.salesmenu import*
from functions.create.createsale import*
from functions.saleshistory import*
import time
import pickle

users = {}

try:
    arqUser = open("users.dat", "rb")
    users = pickle.load(arqUser)
    arqUser.close()
except:
    arqUser = open("users.dat", "wb")
    arqUser.close()
 
sales = {}

try:
    arqSales = open("sales.dat", "rb")
    sales = pickle.load(arqSales)
    arqSales.close()
except:
    arqSales = open("sales.dat", "wb")
    arqSales.close()

end = False

while end == False:
    option = homeMenu()
    
    if option == '1':
        while end == False:
            option = salesMenu()
            if option == '1':
                clear()
                creatSale(sales)
            elif option == '2':
                clear()
                salesHistory(sales)
            elif option == '0':
                clear()
                end = True
            else:
                clear()
                print('Opção invalida!!')
                time.sleep(1)
            
        end = False
    elif option == '2':
        while end == False:
            option = customerMenu()
            if option == '1':
                clear()
                create_user(users)
                print(users)
            elif option == '2':
                clear()
                search_user(users)
            elif option == '3':
                clear()
                upgrade_user(users)
            elif option == '4':
                clear()
                del_user(users)
            elif option == '0':
                clear()
                end = True
            else:
                clear()
                print('Opção invalida!!')
                time.sleep(1)
        end = False
    elif option == '0':
        clear()
        print('Fim do programa')
        end = True
    else:
        clear()
        print('Opção invalida!!')
        time.sleep(1)