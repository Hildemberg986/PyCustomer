#Função para alterar clientes 
def upgrade_user(users):
    from functions.clear import clear
    from functions.datebase import datebase
    from functions.validations.checkerEmail import checker_email
    sale = None
    sales = None
    option = 'update user'

    #Loop para pesquisar usuario e alteralo
    while True:
        clear()
        id_user = input('Digite o cpf do cliente que deseja atualizar... ')
        clear()

        #Pesquisa se o usuario existe e atribui uma resposta para user
        user = users.get(id_user)

        #Checa se o usuario existe
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

            #Define quais dados o usuario ira mudar
            if choice == 's':

                al_name = input('Gostaria de alterar o nome do cliente ? s/n ')
                clear()

                #Define se o usuario ques mudar o nome
                if al_name == 's':
                    name = input("Novo nome do cliente... ")
                    clear()
                else:
                    #Deixa o mesmo nome
                    name = user[0]

                al_email = input('Gostaria de alterar o e-mail do cliente? s/n ')
                clear()

                #Define se o usuario ques mudar o email
                if al_email == 's':
                    email = input("Novo email do cliente... ")
                    checkerEmail = checker_email(email)

                    #Loop para digitar um email valido
                    while checkerEmail  == False: 
                        clear()
                        print('email invalido')
                        print()
                        email = input("Digite seu email... ")
                        
                        #Checa se o email é valido
                        checkerEmail = checker_email(email)
                    clear()
                else:
                    #Deixa o mesmo email
                    email = user[2]

                #Monta o novo cliente
                user = [name, cpf, email]

                #Envia dados para o salvar no banco de dados
                datebase(sale,user,sales, users, option)

                break
            else:
                choice = 'n'
        else:
            print('Cliente não encontrado...') 
            choice = input('Gostaria de tentar de novo ? s/n ')
        if choice == 'n':
            break
    

         
    
    

        