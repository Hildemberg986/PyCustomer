import time
from functions.Generic_functions.clear import clear
from functions.validations.CPFDuplicacion import CPFDuplication
from functions.validations.CheckerCPF import ChekerCPF


def CollectValidCPF(name : str) -> str:
    start= True
    while start == True:
        cpf = str(input("Digite seu CPF... "))
        
        cpf = ''.join(filter(str.isdigit, cpf))
        
        if ChekerCPF(cpf) and CPFDuplication(cpf):
            return cpf
        
        elif not ChekerCPF(cpf):
            clear()
            print("\t\t\tCPF invalido, Por favor digite um CPF valido...")
            time.sleep(3)
            clear()
            print('==================================')
            print('====== CADASTRO  DE CLIENTE ======')
            print('==================================')
            print('')
            
            print('Digite seu Nome...',name)
            
        elif not CPFDuplication(cpf):
            cpf1 = "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
            clear()
            print(f"\t\t\tCliente com CPF {cpf1} já está cadastrado...")
            time.sleep(3)
            clear()
            print('==================================')
            print('====== CADASTRO  DE CLIENTE ======')
            print('==================================')
            print('')
            
            print('Digite seu Nome...',name)