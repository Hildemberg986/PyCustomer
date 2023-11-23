def adminLoginScreen():
    from functions.Generic_functions.clear import clear
    clear()
    print('==================================')
    print('==== LOGIN COMO ADMINISTRADOR ====')
    print('==================================')
    print('')
    id_do_usuario = input('ID do usuario...')
    key = input('Senha...')
    return id_do_usuario,key