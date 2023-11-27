from functions.Generic_functions.clear import clear
from functions.validations.LoginValidation import LoginValidation


def ClientLoginScreen() -> tuple:
    clear()
    print('==================================')
    print('======= LOGIN COMO CLIENTE =======')
    print('==================================')
    print('')
    cpf = input('CPF do usuario...')
    cpf = ''.join(filter(str.isdigit, cpf))
    key = input('Senha...')
    if LoginValidation(cpf,key):
        return cpf, True
    return cpf, False