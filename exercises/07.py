#  Given two integer numbers return their product. If the product is greater than 1000, then return their sum
#  Exercise 1 from https://pynative.com/python-basic-exercise-for-beginners/

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# product = num1 * num2
# if product > 1000:
#     sum = num1 + num2
#     print(sum)
# else:
#     print(product)

"----------------------------"

def numResult(num1, num2):
    product = num1 * num2
    if product > 1000:
        sum = num1 + num2
        return sum
    else:
        return product

print(numResult(10, 2))
print(numResult(2, 2))
print(numResult(100, 2000))
print(numResult(5000, 8000))
print(numResult(1, 0))
print(numResult(0, 0))
