import time
from functions.Generic_functions.clear import clear
from functions.validations.CheckerCPF import ChekerCPF


def CollectValidCPF(name : str) -> str:
    start= True
    while start == True:
        cpf = str(input("Digite seu CPF... "))
        if ChekerCPF(cpf):
            return cpf
        elif ChekerCPF(cpf) == False:
            clear()
            print("\t\t\tCPF invalido, Por favor digite um CPF valido...")
            time.sleep(3)
            clear()
            print('==================================')
            print('====== CADASTRO  DE CLIENTE ======')
            print('==================================')
            print('')
            
            print('Digite seu Nome...',name)