#Função para printar menu inicial
from functions.Generic_functions.clear import clear


def homeMenu():
    clear()
    print('==================================')
    print('========  MENU   INICIAL  ========')
    print('==================================')
    print('   1-> Login')
    print('   2-> Sobre')
    print('   3-> Equipe')
    print('   0-> Sair')
    print('')
    
    try:
        option = int(input('Escolha sua opção: '))
    except ValueError:
        option = int(99999)
        
    return option