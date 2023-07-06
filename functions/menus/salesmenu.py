#Função para printar menu de vendas
def salesMenu():
    from functions.clear import clear
    clear()
    print('==================================')
    print('========  MENU DE VENDAS  ========')
    print('==================================')
    print('   1 - NOVA VENDA')
    print('   2 - HISTORICO DE VENDAS MENSAL')
    print('   0 - VOLTAR')
    option = input('Escolha sua opção ? ')
    return option