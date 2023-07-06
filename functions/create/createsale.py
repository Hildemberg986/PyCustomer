#Função para montar venda
def creatSale(sales):
    #importando funções
    import time
    from functions.clear import clear
    from functions.datebase import datebase

    option = "sale"
    user = None
    users = None

    value = float(input('valor da venda ? '))
    clear()

    paymentmethod = input('qual o metodo de pagamento ? ')
    clear()
    
    #Monta a venda para enviar ao banco de dados 
    sale = [value, paymentmethod]
    
    #Chama a função que salva no banco de dados 
    datebase(sale,user,sales, users, option)

    print('Nova venda cadastrada!')
    time.sleep(1)