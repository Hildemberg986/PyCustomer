def del_user():
    from functions.clear import clear
    import pickle

    Users = {}

    try:
        arqUser = open('Users.dat', 'rb')
        Users = pickle.load(arqUser)
        arqUser.close()
    except:
        arqUser = open('Users.dat', 'wb')
        arqUser.close()

    fim = 0
    while fim != '0':
            search_del_user = input('Qual o id do usuario que gostaria de deletar ? (digite exit caso nâo queira deletar nem um usuario) ')
            clear()
            if search_del_user in Users:
                user = Users[search_del_user]
                print(user) 
                escolha = input('Gostaria mesmo de excluir esse usuario ? s/n ')
                if escolha == 's':
                    del Users[search_del_user]
                    arqUser = open("Users.dat", "wb")
                    pickle.dump(Users, arqUser)
                    arqUser.close()
                    print('Usuario deletado')
                else:
                    print('Usuario não deletado') 
                break
                    
            elif search_del_user == 'exit':
                break
            else:
                print('Chave não encontrada')