import pandas as pd



def SaveClient(cpf : str, name : str, email : str):
    try:
        # Tentar carregar um DataFrame existente
        df = pd.read_excel('dados.xlsx', dtype={'CPF': str, 'Nome': str, 'Email':str})
    except FileNotFoundError:
        # Se o arquivo não existir, criar um novo DataFrame
        df = pd.DataFrame(columns=['CPF', 'Nome', 'Email'])
    
    new_client = pd.DataFrame({'CPF': [cpf], 'Nome': [name], 'Email': [email]})
    df = df._append(new_client, ignore_index=True)
    
    df.to_excel('dados.xlsx', index=False)