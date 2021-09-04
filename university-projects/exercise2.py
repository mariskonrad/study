# função que irá criar o e-mail
def criarEmail(nome, sobrenome, num):
    '''
    Cria um e-mail com a primeira letra do nome do usuário, seu sobrenome e os dois
    últimos números do seu RU.

    :nome: string
    :sobrenome: string
    :num: string
    '''
    # converter o input do usuário em letras minúsculas
    nome = nome.lower()
    sobrenome = sobrenome.lower()
    # pegar a primeira letra do nome do usuário
    letraNome = nome[0]
    email = letraNome + sobrenome + num + '@algoritmos.com.br'
    return email

# Programa principal
# Pede o input do usuário e checa se é um input válido
nome = input('Qual seu nome? ')
while not nome.isalpha():
    print('Dígitos inválidos. Digite apenas letras.')
    nome = input('Qual seu nome? ')

sobrenome = input('Qual seu sobrenome? ')
while not sobrenome.isalpha():
    print('Dígitos inválidos. Digite apenas letras.')
    sobrenome = input('Qual seu sobrenome? ')

num = input('Quais os dois últimos dígitos do seu RU? ')
while len(num) != 2 or (not num.isdigit()):
    print('Dígitos inválidos. Digite apenas 2 números.')
    num = input('Quais os dois últimos dígitos do seu RU? ')

# Mostra a mensagem para o usuário na tela com o e-mail criado
print('{}, seu e-mail é '.format(nome) + criarEmail(nome, sobrenome, num))
