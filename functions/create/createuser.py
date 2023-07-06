#Função para montar venda
def create_user(users):
    from functions.datebase import datebase
    from functions.validations.checkerCPF import validar_cpf
    from functions.clear import clear
    from functions.validations.checkerEmail import checker_email
    import time

    option = 'user'
    sales = None
    sale = None

    name = input("Nome do novo cliente... ")
    clear()
    
    cpf = input("Digite seu cpf... ")
    clear()

    #Checa o CPF, se é valido e não duplicado
    checkerCPF = validar_cpf(cpf, users)
    
    while checkerCPF  == False or checkerCPF == 'double': 
        clear()
        if checkerCPF == False:
            print('cpf invalido')
            print()
        elif checkerCPF == 'double':
            print('cpf cadastrado em outro cliente')
            print()
            
        cpf = input("Digite seu cpf... ")
        checkerCPF = validar_cpf(cpf, users)
    clear()
    
    email = input('Digite seu e-mail... ')

    #Checa o email, se é valido
    checkerEmail = checker_email(email)
    while checkerEmail  == False: 
        clear()
        print('email invalido')
        print()
        email = input("Digite seu email... ")
        checkerEmail = checker_email(email)
    clear()
    
    #Monta o cliente para enviar ao banco de dados 
    user = [name, cpf, email]
    
    datebase(sale,user,sales, users, option)
    
    print ('Novo cliente cadastrado!')
    time.sleep(1)