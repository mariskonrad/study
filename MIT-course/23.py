# Consider the following sequence of expressions:

# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')

# write a procedure, called biggest, which returns the key corresponding to the entry
# with the largest number of values associated with it.
# If there is more than one such entry, return any one of the matching keys.

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    big = 0
    bigger = ''
    for k in aDict:
        if len(aDict[k]) >= big:
            big = len(aDict[k])
    return bigger


aDict = {'a': [15, 2], 'c': [18, 13, 10, 11, 10], 'b': [7, 3, 14, 1, 18, 5, 13, 10, 2, 11], 'd': [18]}
print(biggest(aDict))
