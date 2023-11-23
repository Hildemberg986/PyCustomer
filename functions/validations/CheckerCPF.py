#Validação do cpf criada pelo chat GPT, menos o de testar CPF duplicado
def ChekerCPF(cpf : str):
    # Remover caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificar se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    # Verificar o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0

    if int(cpf[9]) != digito1:
        return False

    # Verificar o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0

    if int(cpf[10]) != digito2:
        return False
    # CPF válido
    return True