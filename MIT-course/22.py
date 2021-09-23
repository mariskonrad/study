# Consider the following sequence of expressions:
# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')
# We want to write some simple procedures that work on dictionaries to return information.
# Write a procedure called how_many, which returns the sum of the number of values
# associated with a dictionary.

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    s = []
    for i in aDict.values():
        s.extend(i)
    return len(s)

print(how_many({'B': [15], 'u': [10, 15, 5, 2, 6]}))
