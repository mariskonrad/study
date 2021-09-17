while True:
    # Perguntar se o usuário deseja iniciar o programa. O loop encerra quando o usuário digita valores válidos
    resp = ''
    while True:
        resp = input('Inserir dados no programa? (S)im / (N)ão: ')
        resp = resp.lower()
        if resp == 's' or resp == 'n':
            break

    # Condição que encerra o programa
    if resp == 'n':
        print('Encerrando o programa...')
        break

    else:
        # Pedir input do nome do usuário até que ele digite apenas letras
        nome = ""
        while True:
            nome = input('Qual seu nome? ')
            if nome.isalpha():
                break
            print('Digite apenas letras.')

        # Pedir input da nota do usuário até que ele digite apenas números válidos e tratar erro de exceção.
        nota = 0
        while True:
            try:
                nota = float(input('Digite sua nota: '))
                if nota >= 0 and nota <= 10:
                    break
                print('Digite apenas números de 0 a 10.')
            except:
                print('Digite um número válido.')
                continue

        # Atribuir o conceito ao input recebido do usuário
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

        # Imprimir mensagem na tela
        print('O(a) aluno(a) {} tirou nota {} e se enquadra no conceito {}.' .format(nome, nota, conceito))


