import time
from functions.Generic_functions.clear import clear


def CollectValue(produto : str):
    start = True
    while start != False:
        clear()
        print(f"Nome do Produto...{produto}")
        valor = input("valor do produto... ")
        try:
            valor = float(valor)
            validation = True
        except ValueError:
            clear()
            print("\t\t\tDigite um valor valido... ")
            time.sleep(3)
            validation = False
        if validation:
            return valor