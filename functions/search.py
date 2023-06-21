def colar():
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

for cpf in Users:
    print(cpf)