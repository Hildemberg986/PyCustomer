import time
from functions.Generic_functions.clear import clear
from functions.validations.CheckerEmail import CheckerEmail


def CollectValidEmail(name : str,cpf : str) -> str:
    start= True
    while start == True:
        email = str(input("Digite seu Email... "))
        if CheckerEmail(email):
            return email
        elif CheckerEmail(email) == False:
            clear()
            print("\t\t\tEmail invalido, Por favor digite um Email valido...")
            time.sleep(3)
            clear()
            print('==================================')
            print('====== CADASTRO  DE CLIENTE ======')
            print('==================================')
            print('')
            print('Digite seu Nome...',name)
            print('Digite seu CPF...',cpf)