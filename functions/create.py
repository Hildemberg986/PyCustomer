def create_user():
    from functions.duplicatecpfchecker import duplicate_cpf_checker
    from functions.checker import validar_cpf
    from functions.clear import clear
    import pickle
    import time

    Users = {}

    try:
     arqUser = open("Users.dat", "rb")
     Users = pickle.load(arqUser)
     arqUser.close()
    except:
     arqUser = open("Users.dat", "wb")
     arqUser.close()
    

    name = input("Nome do novo usuario... ")
    clear()
    cont = 0
    while cont == 0:
        cpf = input("Digite seu cpf... ")
        cpf = ''.join(filter(str.isdigit, cpf))
        checker_cpf = validar_cpf(cpf)
        if checker_cpf:
            if duplicate_cpf_checker(cpf):
                clear()
                print("CPF já cadastrado em outro usuário")
            else:
                break
        else:
            clear()
            print('CPF inválido!!')
    clear()
    email = input("Digite seu e-mail... ")
    clear()
    print('Novo usuario cadastrado')
    time.sleep(3)

    user = [name, cpf, email]
    return user