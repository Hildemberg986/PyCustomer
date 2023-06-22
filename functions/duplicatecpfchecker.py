def duplicate_cpf_checker(cpf):

    import pickle

    Users = {}
    try:
        arqUser = open("Users.dat", "rb")
        Users = pickle.load(arqUser)
        arqUser.close()
    except:
        arqUser = open("Users.dat", "wb")
        arqUser.close()
    for user in Users.values():
        if cpf in user:
            return True
            break
