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

#Importa o dicionario users do banco de dados
users = {}

try:
    arqUser = open("users.dat", "rb")
    users = pickle.load(arqUser)
    arqUser.close()
except:
    arqUser = open("users.dat", "wb")
    arqUser.close()

#Importa o dicionario sales do banco de dados
sales = {}

try:
    arqSales = open("sales.dat", "rb")
    sales = pickle.load(arqSales)
    arqSales.close()
except:
    arqSales = open("sales.dat", "wb")
    arqSales.close()

endP = False
#Loop para o menu principal
while endP == False:
    end = False
    #Define uma opção
    option = homeMenu()
    
    #Define qual opção entrar
    if option == '1':
        
        #Loop para o menu de vendas
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
    #Loop para o menu de cliente
    elif option == '2':
        
        #Loop para o menu de clientes
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

            #Sai do loop
            elif option == '0':
                clear()
                end = True
            else:
                clear()
                print('Opção invalida!!')
                time.sleep(1)
        end == False
    #Sai do loop
    elif option == '0':
        clear()
        print('Fim do programa')
        endP = True
    else:
        clear()
        print('Opção invalida!!')
        time.sleep(1)