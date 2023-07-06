#Função para printar menu de cliente
def customerMenu():
    from functions.clear import clear
    clear()
    print('==================================')
    print('========  MENU   CLIENTE  ========')
    print('==================================')
    print('   1 - CADASTRAR CLIENTE')
    print('   2 - PESQUISAR CLIENTE')
    print('   3 - MODIFICAR CLIENTE')
    print('   4 - DELETAR CLIENTE')
    print('   0 - VOLTAR')
    option = input('Escolha sua opção ? ')
    return option