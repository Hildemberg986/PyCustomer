def datebase(add):
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

    Users[id_user] = add
    
    arqUser = open("Users.dat", "wb")
    pickle.dump(Users , arqUser)
    arqUser.close()
    print (Users)