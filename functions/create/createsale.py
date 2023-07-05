def creatSale(sales):
    from datetime import datetime
    from functions.clear import clear
    import pickle

    data_atual = datetime.today()
    key = data_atual.strftime('''%d%m%Y%H%M%S''')
    
    value = float(input('valor da venda ? '))
    clear()
    paymentmethod = input('qual o metodo de pagamento ? ')
    sale = [value, paymentmethod]
    
    sales[key] = sale
    
    arqSales = open("sales.dat", "wb")
    pickle.dump(sales , arqSales)
    arqSales.close()