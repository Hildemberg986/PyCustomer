def datebase(add):
    import pickle
    from datetime import date
    
    data_atual = date.today()
    Users = {}
    cpf_user = add[1]
    initial_cpf = cpf_user[0:3]
    end_cpf = cpf_user[6:9]
    try:
     arqUser = open("Users.dat", "rb")
     Users = pickle.load(arqUser)
     arqUser.close()
    except:
     arqUser = open("Users.dat", "wb")
     arqUser.close()
    id_user = '{}000{}{}'.format (data_atual.year, initial_cpf, end_cpf) 

    Users[id_user] = add
    
    arqUser = open("Users.dat", "wb")
    pickle.dump(Users , arqUser)
    arqUser.close()
    print (Users)