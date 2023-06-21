def create_user():
    from functions.clear import clear
    import pickle

    Users = {}

    try:
     arqUser = open("Users.dat", "rb")
     Users = pickle.load(arqUser)
     arqUser.close()
    except:
     arqUser = open("Users.dat", "wb")
     arqUser.close()
    id_user = len(Users.keys())

    name = input("Nome do novo usuario... ")
    clear()
    cont = 0
    while cont == 0:
        cpf = input("Digite seu cpf... ")
        print('000' in Users.values())
        if cpf in Users.values():
            clear()
            print("CPF já cadastrado em outro usuário")
        else:
            print('Novo usuário cadastrado')
            cont = 1
    user = [name, cpf]
    return user