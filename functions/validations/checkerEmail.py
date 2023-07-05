def checker_email(email):
    import re
    # Expressão regular para validar o formato do e-mail
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    # Verifica se o email corresponde ao padrão definido
    if re.match(padrao, email):
        return True
    else:
        return False