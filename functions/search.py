def search_user(users):
    from functions.clear import clear
    
    end = False
    while end == False:
        clear()
        id_user = input('Digite o cpf do cliente que deseja buscar... ')
        clear()
        user = users.get(id_user)
        if user != None:
            user ='''
            Nome: {} 
            CPF: {} 
            E-mail: {}'''.format (user[0],user[1],user[2]) 
            print(user)      
            print()
            choice = input('Gostaria de buscar um novo cliente ? s/n ')
        else:
            print('Cliente não encontrado...') 
            choice = input('Gostaria de buscar de novo ? s/n ')
        if choice == 'n':
            end = True
        
