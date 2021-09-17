# Exercise: is in (redo)
# First test the middle character of a string against the character you're looking for (test char)
# If they're the same, we're done.
# If they're not the same, check if test char is smaller than middle char. If so, we need only consider
# the lower half of the string. Otherwise, we only consider the upper half.
# Implement the function which implements the above idea recursively.

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise.
    '''
    if len(aStr) == 0:
        return False

    mid = len(aStr) // 2

    if aStr[mid] == char:
        return True

    if len(aStr) == 1:
        return False

    if char > aStr[mid]:
        return isIn(char, aStr[mid:])

    return isIn(char, aStr[:mid])
