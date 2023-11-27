import pandas as pd

def LoginValidation(cpf: str, Senha : str) -> bool:
    try:
        # Tentar carregar um DataFrame existente
        df = pd.read_excel('login.xlsx', dtype={'CPF': str, 'Senha': str})
    except FileNotFoundError:
        # Se o arquivo não existir, criar um novo DataFrame
        df = pd.DataFrame(columns=['CPF', 'Senha'])
    for i, f in zip(df['CPF'], df['Senha']):
        i = str(i)
        f = str(f)
        if i == cpf and f == Senha:
            return True
    return False