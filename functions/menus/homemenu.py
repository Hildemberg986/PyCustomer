def homeMenu():
    from functions.clear import clear
    clear()
    print('==================================')
    print('========  MENU   INICIAL  ========')
    print('==================================')
    print('   1 - MENU DE VENDAS')
    print('   2 - MENU CLIENTE')
    print('   0 - SAIR')
    option = input('Escolha sua opção ? ')
    return option