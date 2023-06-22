from functions.create import *
from functions.search import *
from functions.delete import *
from functions.clear import *
from functions.datebase import *
from functions.checker import *


fim = 0
while fim != '0':
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
        add = create_user()
        datebase(add)
    elif option == '2':
        clear()
        search_user()
    elif option == '3':
        print('opçao 3')
    elif option == '4':
        clear()
        del_user()
    elif option == '0':
        clear()
        print ('Programa encerrado!')
        break