def create_user(users):
    from functions.datebase import datebase
    from functions.checkerCPF import validar_cpf
    from functions.clear import clear
    import time
    
    name = input("Nome do novo cliente... ")
    clear()
    
    cpf = input("Digite seu cpf... ")
    clear()
    
    checker = validar_cpf(cpf, users)
    
    while checker  == False or checker == 'double': 
        if checker == False:
            print('cpf invalido')
            print()
        elif checker == 'double':
            print('cpf cadastrado em outro cliente')
            print()
            
        cpf = input("Digite seu cpf... ")
        checker = validar_cpf(cpf, users)
    clear()
    
    email = input('Digite seu e-mail... ')
    clear()
    
    user = [name, cpf, email]
    
    datebase(user,users)
    
    print ('Novo cliente cadastrado!')
    time.sleep(1)