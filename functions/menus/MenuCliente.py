from functions.Generic_functions.clear import clear


def MenuCliente() -> int:
    clear()
    print('==================================')
    print('========  MENU   INICIAL  ========')
    print('==================================')
    print('   1-> Comprar')
    print('   2-> Pesquisar Compras')
    print('   0-> Sair')
    print('')
    try:
        option = int(input('Escolha sua opção: '))
    except ValueError:
        option = int(99999)
        
    return option