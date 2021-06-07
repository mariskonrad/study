#   Accept number from user and calculate the sum of all number from 1 to a given number

s = 0
n = int(input("Type a number: "))
for i in range(n + 1):
    s += i
print("Sum is", s)
