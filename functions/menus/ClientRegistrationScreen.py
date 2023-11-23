from functions.Generic_functions.CollectValidCPF import CollectValidCPF
from functions.Generic_functions.CollectValidEmail import CollectValidEmail
from functions.Generic_functions.clear import clear


def ClientRegistrationScreen():
    clear()
    print('==================================')
    print('====== CADASTRO  DE CLIENTE ======')
    print('==================================')
    print('')
    name = str(input('Digite seu Nome... '))
    cpf = CollectValidCPF(name)
    email = CollectValidEmail(name,cpf)
    
    