# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import sys

def is_multiple(a, b):
    return a % b == 0

def sum_multiples(max):
   
    sum = 0

    for i in range(max):
        if is_multiple(i, 3) or is_multiple(i, 5):
            sum = sum + i
    
    return sum

max_str = sys.argv[1]
max = int(max_str)
print(sum_multiples(max))
