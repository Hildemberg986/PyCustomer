#Função para dicionarios no banco de dados 
def datebase(sale,user,sales, users, option):
    from datetime import datetime
    import pickle

    #Define qual banco de dados salvar 
    if option == "user" or 'update user':

        #Extrai o CPF do cliente para aser usado como key no dicionario
        cpf_user = user[1]

        #Implementa o novo user no dicionario users
        users[cpf_user] = user

        #Salva o dicionario no arquivo .dat em binario
        arqUser = open("users.dat", "wb")
        pickle.dump(users , arqUser)
        arqUser.close()
    elif option == "sale":

        #Puxa a data atual da biblioteca datetime
        data_atual = datetime.today()

        #Gera a key usando a data e hora 
        key = data_atual.strftime('''%d%m%Y%H%M%S''')

        #Implementa a nova sale no dicionario sales
        sales[key] = sale

        #Salva o dicionario no arquivo .dat em binario
        arqSales = open("sales.dat", "wb")
        pickle.dump(sales , arqSales)
        arqSales.close()