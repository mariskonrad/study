# Função que irá criar o e-mail
def criarEmail(nome, sobrenome, num):
    '''
    Retorna o e-mail com a primeira letra do nome do usuário, seu sobrenome e os dois
    últimos números do seu RU.

    nome: string
    sobrenome: string
    num: string
    '''
    # Converte o input do usuário em letras minúsculas
    nome = nome.lower()
    sobrenome = sobrenome.lower()
    # Pega a primeira letra do nome do usuário e concatena formando o e-mail
    letraNome = nome[0]
    email = letraNome + sobrenome + num + '@algoritmos.com.br'
    return email

# Programa principal
# Pede o input do usuário até que ele seja válido
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

# Imprime a mensagem com o e-mail criado
print('{}, seu e-mail é '.format(nome) + criarEmail(nome, sobrenome, num))
