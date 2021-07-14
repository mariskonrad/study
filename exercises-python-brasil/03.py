#  Faça um programa, com uma função que necessite de um argumento.
#  A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def positiveOrNegative(n):
    if n <= 0:
        return "N"
    else:
        return "P"

positiveOrNegative(0)
