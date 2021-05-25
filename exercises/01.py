# Fazer um programa que recebe um número da linha de comando e printa a soma de 1 até esse número, inclusive.

import sys

def find_sum(max):    
    sum = 0
    for i in range(max + 1):
        sum = sum + i
    return sum

if len(sys.argv) == 1:
    max_str = input("Digite um número: ")
elif len(sys.argv) == 2:
    max_str = sys.argv[1]
else:
    
max = int(max_str)
print(find_sum(max))
