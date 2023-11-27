import pandas as pd


def SaveLogin(cpf : str, senha : str):

    try:
        # Tentar carregar um DataFrame existente
        df = pd.read_excel('login.xlsx', dtype={'CPF': str, 'Senha': str})
    except FileNotFoundError:
        # Se o arquivo não existir, criar um novo DataFrame
        df = pd.DataFrame(columns=['CPF', 'Senha'])
    
    new_client = pd.DataFrame({'CPF': [cpf], 'Senha': [senha]})
    df = df._append(new_client, ignore_index=True)
    
    df.to_excel('login.xlsx', index=False)