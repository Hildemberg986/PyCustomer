from functions.Generic_functions.clear import clear


def MenuCliente(cpf : str) -> int:
    clear()
    cpf1 = "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
    print( '==================================')
    print( '========  MENU   CLIENTE  ========')
    print( '==================================')
    print(f'====== Login: {cpf1} =====')
    print( '==================================')
    print('   1-> Comprar')
    print('   2-> Pesquisar Compras')
    print('   0-> Sair')
    print('')
    try:
        option = int(input('Escolha sua opção: '))
    except ValueError:
        option = int(99999)
        
    return option