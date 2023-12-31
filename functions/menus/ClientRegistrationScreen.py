from functions.Generic_functions.CollectValidCPF import CollectValidCPF
from functions.Generic_functions.CollectValidEmail import CollectValidEmail
from functions.Generic_functions.clear import clear
from functions.save_functions.SaveClient import SaveClient
from functions.save_functions.SaveLogin import SaveLogin

def ClientRegistrationScreen() -> None:
    clear()
    print('==================================')
    print('====== CADASTRO  DE CLIENTE ======')
    print('==================================')
    print('')
    name = str(input('Digite seu Nome... '))
    cpf = CollectValidCPF(name)
    email = CollectValidEmail(name,cpf)
    senha = input(str("Digite uma senha para login... "))
    SaveClient(cpf,name,email)
    SaveLogin(cpf, senha)