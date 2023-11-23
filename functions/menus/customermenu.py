#Função para printar menu de cliente
from functions.Generic_functions.clear import clear


def customerMenu():
    clear()
    print('==================================')
    print('========== MENU   LOGIN ==========')
    print('==================================')
    print('   1 - Logar Como Administrador')
    print('   2 - Logar Como cliente')
    print('   3 - Cadastrar Novo Ususario')
    print('   0 - Voltar')
    print('')
    try:
        option = int(input('Escolha sua opção: '))
    except ValueError:
        option = int(99999)
    return option