def datebase(user, users):
    import pickle
    cpf_user = user[1]

    users[cpf_user] = user
    
    arqUser = open("users.dat", "wb")
    pickle.dump(users , arqUser)
    arqUser.close()