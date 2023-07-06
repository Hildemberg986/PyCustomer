#Funação para imprimir tabela de vendas mensal
def salesHistory(sales):
    from functions.clear import clear

    #Loop para o usuario digitar um ano valido 
    while True:
        year = input('Qual o ano que deseja buscar (YYYY) ? ')

        #conta quantos digitos o usuario digitou
        yearc = len(year)

        #verifica se o usuario colocou um ano valido
        if yearc == 4 and (year[0] == "2" or year[0] == "1"):
            break
        else:
            clear()
            print('Digite um ano valido !')
    clear()

    #Loop para o usuario digitar um més valido 
    while True:
        month = input('Qual o mês que deseja buscar (MM) ? ')

        #conta quantos digitos o usuario digitou
        monthc = len(month) 

        #verifica se o usuario colocou um més valido
        if monthc == 2 and (month[0] == '0' or month[0] == "1" or month[0] == "2" or month[0] == "3"):
            break
        else:
            clear()
            print('Digite um mês valido!')
    clear()

    cont = True
    saleExists = False

    #Pecorre a lista de vendas para ver se a vendas 
    for dhs in sales:
        #Busca a venda no ano e més desejado e printa na tela
        if year == dhs[4:8] and month == dhs[2:4]:

            #Cria o cabeçario da tabela de venda 
            if cont == True:
                saleExists = True
                tabela = '''id da venda    |Valor da venda  | Tipo de venda'''
                print('---------------------------------------------')
                print(tabela)
                print('---------------------------------------------')

                #Para printar o cabeçario apenas uma vez
                cont = False
            
            #Seleciona a venda no dicionario sales
            sale = sales.get(dhs)
            
            #Monta a valor da sale com o R$ antes do valor
            value = "R$ "+str(sale[0])

            #completa o tamanho da string para 15 caracteres apos o valor, com um espaço em branco para manter a formatação da tabela
            value = value.ljust(15, ' ')

            #Ordena a lista com os espaçamentos corretos da tabela
            saleM ='''{} |{} |{}'''.format (dhs,value,sale[1])

            #Imprime a venda do ano e més escolhido
            print(saleM)

    #checa se a vendas 
    if saleExists == False:
        print ('Não a vendas no mês pesquisado!') 

    print()
    input('Pressione Enter para continuar...')