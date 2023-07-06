#fução para pesquisar cliente
def search_user(users):
    from functions.clear import clear
    
    #loop para sair do loop
    while True:
        
        clear()
        id_user = input('Digite o cpf do cliente que deseja buscar... ')
        clear()

        #Checa se o cliente foi cadastardo e atribui um valor para user
        user = users.get(id_user)

        #Checa se usuario existe ou não
        if user != None:
            user ='''
            Nome: {} 
            CPF: {} 
            E-mail: {}'''.format (user[0],user[1],user[2]) 
            print(user)      
            print()
            
            #Define a saida do loop ou não
            choice = input('Gostaria de buscar um novo cliente ? s/n ')
        else:
            print('Cliente não encontrado...') 

            #Define a saida do loop ou não
            choice = input('Gostaria de buscar de novo ? s/n ')

        #Define a saida do loop
        if choice == 'n':
            break
        
