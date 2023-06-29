def del_user(users):
    from functions.clear import clear
    import pickle
    import time
    
    end = False
    while end == False:
        clear()
        id_user = input('Digite o cpf do Cliente que deseja deletar... ')
        clear()
        user = users.get(id_user)
        if user != None:
            user ='''
            Nome: {} 
            CPF: {} 
            E-mail: {}'''.format (user[0],user[1],user[2]) 
            print(user)      
            print()
            choice = input('Gostaria de deletar esse cliente ? s/n ')
            if choice == 's':
                users.pop(id_user)
                print('Cliente deletado com sucesso!!')
                time.sleep(1)
                choice = 'n'
                arqUser = open("users.dat", "wb")
                pickle.dump(users , arqUser)
                arqUser.close()
        else:
            print('Cliente não encontrado...') 
            choice = input('Gostaria de buscar de novo ? s/n ')
        if choice == 'n':
            end = True