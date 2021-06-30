# Write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary.

def how_many(aDict):
    result = 0
    for key in aDict:
        result += len(aDict[key])
    return result
    