def salesHistory(sales):
    from functions.clear import clear
    while True:
        year = input('Qual o ano que deseja buscar (YYYY) ? ')
        yearc = len(year) 
        if yearc == 4 and (year[0] == "2" or year[0] == "1"):
            break
        else:
            clear()
            print('Digite um ano valido !')
    clear()
    while True:
        month = input('Qual o mês que deseja buscar (MM) ? ')
        monthc = len(month) 
        if monthc == 2 and (month[0] == '0' or month[0] == "1" or month[0] == "2" or month[0] == "3"):
            break
        else:
            clear()
            print('Digite um mês valido!')
    clear()
    cont = True
    saleExists = False
    for dhs in sales:
        if year == dhs[4:8] and month == dhs[2:4]:
            if cont == True:
                saleExists = True
                tabela = '''id da venda    |Valor da venda  | Tipo de venda'''
                print('---------------------------------------------')
                print(tabela)
                print('---------------------------------------------')
                cont = False
            sale = sales.get(dhs)
            value = "R$ "+str(sale[0]) 
            value = value.ljust(15, ' ')
            saleM ='''{} |{} |{}'''.format (dhs,value,sale[1]) 
            print(saleM)
    if saleExists == False:
        print ('Não a vendas no mês pesquisado!') 
    print()
    input('Pressione Enter para continuar...')