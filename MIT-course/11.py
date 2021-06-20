
# somar uma sequência de números usando iteração e depois recursão

def iterativeSum (n):
   result = 0
   for i in range(n+1):
      result = result + i
   return result

def recursiveSum(n):
   if n == 0:
      return 0
   return n + recursiveSum(n-1)

print(iterativeSum(5))
print(iterativeSum(20))
print(iterativeSum(100))
print(iterativeSum(1))
print(iterativeSum(0))
print("-------------------")
print(iterativeSum(5))
print(iterativeSum(20))
print(iterativeSum(100))
print(iterativeSum(1))
print(iterativeSum(0))
