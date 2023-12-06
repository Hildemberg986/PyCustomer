import locale
import pandas as pd



def SaveSale(cpf : str, produto : str, valor : float, id_venda:str):
    
    try:
        # Tentar carregar um DataFrame existente
        df = pd.read_excel('vendas.xlsx', dtype={'CPF': str, 'Produto': str, 'Valor':str, 'id_venda':str})
    except FileNotFoundError:
        # Se o arquivo não existir, criar um novo DataFrame
        df = pd.DataFrame(columns=['CPF','Produto','Valor','id_venda'])
    
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    
    valor_formatado = locale.format('%.2f', valor)
    
    new_client = pd.DataFrame({'CPF': [cpf], 'Produto': [produto], 'Valor': [valor_formatado], 'id_venda':[id_venda]})
    df = pd.concat([df, new_client], ignore_index=True)
    
    df.to_excel('vendas.xlsx', index=False)