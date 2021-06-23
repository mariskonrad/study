# Exercise gdc recur

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return b / gcdRecur(b, a % b)

gcdRecur(528, 240)
    