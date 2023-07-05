def upgrade_user(users):
    from functions.clear import clear
    from functions.datebase import datebase
    from functions.validations.checkerEmail import checker_email
    end = False
    while end == False:
        clear()
        id_user = input('Digite o cpf do cliente que deseja atualizar... ')
        clear()
        user = users.get(id_user)
        if user != None:
            cpf = user[1]
            copy_user ='''
            Nome: {} 
            CPF: {} 
            E-mail: {}'''.format (user[0],user[1],user[2]) 
            print(copy_user)      
            print()
            choice = input('Gostaria de modificar o cliente? s/n ')
            clear()
            if choice == 's':
                al_name = input('Gostaria de alterar o nome do cliente ? s/n ')
                clear()
                if al_name == 's':
                    name = input("Novo nome do cliente... ")
                    clear()
                else:
                    name = user[0]
                al_email = input('Gostaria de alterar o e-mail do cliente? s/n ')
                clear()
                if al_email == 's':
                    email = input("Novo email do cliente... ")
                    checkerEmail = checker_email(email)
                    while checkerEmail  == False: 
                        clear()
                        print('email invalido')
                        print()
                        email = input("Digite seu email... ")
                        checkerEmail = checker_email(email)
                    clear()
                else:
                    email = user[2]
                user = [name, cpf, email]    
                datebase(user, users)
                end = True
            else:
                choice = 'n'
        else:
            print('Cliente não encontrado...') 
            choice = input('Gostaria de tentar de novo ? s/n ')
        if choice == 'n':
            end = True
    

         
    
    

        