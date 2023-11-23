from functions.Generic_functions.clear import clear


def ClientLoginScreen():
    clear()
    print('==================================')
    print('======= LOGIN COMO CLIENTE =======')
    print('==================================')
    print('')
    id_do_usuario = input('ID do usuario...')
    key = input('Senha...')
    return id_do_usuario,key