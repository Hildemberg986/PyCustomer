def create_user(users):
    from functions.datebase import datebase
    from functions.validations.checkerCPF import validar_cpf
    from functions.clear import clear
    from functions.validations.checkerEmail import checker_email
    import time
    
    name = input("Nome do novo cliente... ")
    clear()
    
    cpf = input("Digite seu cpf... ")
    clear()
    
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
    checkerEmail = checker_email(email)
    while checkerEmail  == False: 
        clear()
        print('email invalido')
        print()
        email = input("Digite seu email... ")
        checkerEmail = checker_email(email)
    clear()
    
    user = [name, cpf, email]
    
    datebase(user,users)
    
    print ('Novo cliente cadastrado!')
    time.sleep(1)