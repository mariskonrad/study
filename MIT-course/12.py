
# multiplicar uma sequência de números usando iteração e depois recursão

def iterativeFact(n):
    ans = 1
    for i in range(2, n + 1):
        ans = ans * i
    return ans


def recursiveFact(n):
    if n < 2:
        return 1
    return n * recursiveFact(n - 1)


print(iterativeFact(3))
print(iterativeFact(5))
print(iterativeFact(10))
print(iterativeFact(0))
print(iterativeFact(1))
print(iterativeFact(2))

print("-------------------")

print(recursiveFact(3))
print(recursiveFact(5))
print(recursiveFact(10))
print(recursiveFact(0))
print(recursiveFact(1))
print(recursiveFact(2))

