import time
import pandas as pd

def CPFDuplication(cpf: str) -> bool:
    try:
        # Tentar carregar um DataFrame existente
        df = pd.read_excel('dados.xlsx')
    except FileNotFoundError:
        # Se o arquivo não existir, criar um novo DataFrame
        df = pd.DataFrame(columns=['CPF', 'Nome', 'Email'])

    for i in df['CPF']:
        i = str(i)
        if i == cpf:
            return False
    return True