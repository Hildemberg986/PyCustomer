def create_user():
    from functions.clear import clear
    name = input("Nome do novo usuario... ")
    clear()
    cont = 0
    Users = ["123"]
    while cont == 0:
        cpf = input("Digite seu cpf... ")
        if cpf in Users:
            clear()
            print("CPF já cadastrado em outro usuário")
        else:
            print('Novo usuário cadastrado')
            cont = 1
            NewUser = [name, cpf]
            InputUser = open("User.txt", "a")
            for item in NewUser:
                InputUser.write(item + '\n')
            InputUser.write('\n')
            InputUser.close()
    return name; cpf