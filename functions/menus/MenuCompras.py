from datetime import datetime
from functions.Generic_functions.CollectValue import CollectValue
from functions.Generic_functions.clear import clear
from functions.save_functions.SaveSale import SaveSale


def MenuCompras(cpf : str):
    clear()
    agora = datetime.now()

    formato = "%Y%m%d%H%M%S"
    id_venda = agora.strftime(formato)

    
    produto = str(input("Nome do Produto... "))

    valor = CollectValue(produto)
    
    SaveSale(cpf, produto, valor, id_venda)