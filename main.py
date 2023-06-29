from functions.create import *
from functions.search import *
from functions.delete import *
from functions.clear import *
from functions.datebase import *
from functions.checkerCPF import *
from functions.upgradeuser import *
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

fim = False

while fim == False:
    clear()
    print('==================================')
    print('========  MENU PRINCIPAL  ========')
    print('==================================')
    print('   1 - CADASTRAR CLIENTE')
    print('   2 - PESQUISAR CLIENTE')
    print('   3 - MODIFICAR CLIENTE')
    print('   4 - DELETAR CLIENTE')
    print('   0 - SAIR')
    option = input('Escolha sua opção ? ')
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
        print ('Programa encerrado!')
        fim = True
    else:
        clear()
        print('Opção invalida!!')
        time.sleep(1)