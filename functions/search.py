def search_user():
    import pickle
    from functions.clear import clear
    
    
    Users = {}
    try:
        arqUser = open("Users.dat", "rb")
        Users = pickle.load(arqUser)
        arqUser.close()
    except:
        arqUser = open("Users.dat", "wb")
        arqUser.close()
    fim = 0
    while fim != "0":
        clear()
        searchitem = input('Digite o cpf ou nome do usuario que deseja buscar... ')
        clear()
        for key, user in Users.items():    
            if searchitem in user:
                print()
                User ='''
        id: {} 
        Nome: {} 
        CPF: {} 
        E-mail: {}'''.format (key,user[0],user[1],user[2]) 
                print(User)       
                break
            User = ''

        if User == '':
            escolha = input('Usuario nao encontrado, deseja buscar novanmente ? s/n ')
            if escolha == 'n':
                break
        elif user != "":
            print()
            print()
            input('Precione enter para continuar...')
            break