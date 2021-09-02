# Perguntar se o usuário deseja inserir dados
# checa se o input é um número
while True:
    try:
        resp = int(input("Inserir dados no programa? 0 - Não   1 - Sim "))
    except ValueError:
        print('Dígito inválido. Por favor, insira 0 para "Não" e 1 para "Sim": ')

    # checa se dígitos inseridos são válidos
    while resp != 0 and resp != 1:
        print("Dígitos inválidos.")
        resp = int(input("Inserir dados no programa? 0 - Não   1 - Sim "))

    # encerra o programa
    if resp == 0:
        print("Encerrando o programa...")
        break

    else:
        if resp == 1:
            nome = input("Qual seu nome? ")
            nota = float(input("Digite sua nota: "))
            conceito = ''
            if nota >= 0 and nota <= 2.9:
                conceito = 'E'
            elif nota >= 3 and nota <= 4.9:
                conceito = 'D'
            elif nota >= 5 and nota <= 6.9:
                conceito = 'C'
            elif nota >= 7 and nota <= 8.9:
                conceito = 'B'
            elif nota >= 9 and nota <= 10:
                conceito = 'A'
            print("O(a) aluno(a) {} tirou nota {} e se enquadra no conceito {}." .format(nome, nota, conceito))

# verificar o NameError
