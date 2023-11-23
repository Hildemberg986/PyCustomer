from functions.Generic_functions.clear import clear
from functions.validations.CheckLogin import CheckLogin


def adminLoginScreen():
    start = True
    while start == True:
        clear()
        print('==================================')
        print('==== LOGIN COMO ADMINISTRADOR ====')
        print('==================================')
        print('')
        cpf = input("Insira o CPF: ")
        password = input("Senha: ")
        if CheckLogin(cpf,password) == False:
            option = input("Usuario não encontrado deseja realizar nova busca ? s/n")
            if option != "s":
                start = False
    return 