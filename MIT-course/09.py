# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh

s = "azcdobobegghaklabcdef"
acc = s[0]
best = acc

for i in range(len(s) - 1):
    atual = s[i]
    proximo = s[i+1]
    # se está em ordem alfabetica
    if atual <= proximo:
        acc += proximo
        if len(acc) > len(best):
            best = acc
            
    # se nao esta em ordem alfabetica
    else:
        acc = proximo

print(best)
