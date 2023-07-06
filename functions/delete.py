#função para deletar cliente
def del_user(users):
    from functions.clear import clear
    import pickle
    import time
    
    #Loop para pesquisar usuario e escolher se deseja deletalo
    while True:
        clear()
        id_user = input('Digite o cpf do Cliente que deseja deletar... ')
        clear()
        
        #Pesquisa se o cleiente existe e atribui uma resposta para user
        user = users.get(id_user)

        #Define se o cliente exite ou não
        if user != None:
            user ='''
            Nome: {} 
            CPF: {} 
            E-mail: {}'''.format (user[0],user[1],user[2]) 
            print(user)      
            print()
            choice = input('Gostaria de deletar esse cliente ? s/n ')

            #Define se o cliente e deletado
            if choice == 's':
                #Deleta o cliente
                users.pop(id_user)
                print('Cliente deletado com sucesso!!') 
                time.sleep(1)

                choice = 'n'
                
                #Salva o dicionario sem o cliente excluido
                arqUser = open("users.dat", "wb")
                pickle.dump(users , arqUser)
                arqUser.close()
        else:
            print('Cliente não encontrado...') 
            choice = input('Gostaria de buscar de novo ? s/n ')
        if choice == 'n':
            break