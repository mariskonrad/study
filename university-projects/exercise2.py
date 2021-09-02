def criarEmail(nome, sobrenome, num):
    '''
    Cria um e-mail com a primeira letra do nome do usuário, seu sobrenome e os dois
    últimos números do seu RU.

    nome: string
    sobrenome: string
    num: string
    '''

    letraNome = nome[0]
    texto = "Olá, {} {}! Seu e-mail é {}@algoritmos.com.br" .format(nome, sobrenome, letraNome + sobrenome + num)
    return texto

# Programa principal

nome = input("Qual seu nome? ")
sobrenome = input("Qual seu sobrenome? ")
num = input("Quais os dois últimos dígitos do seu RU? ")
print(criarEmail(nome, sobrenome, num))

# transformar os inputs todos em minusculo
# colocar o ultimo parametro como opcional
