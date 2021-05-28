# create a program that receives a list of numbers and outputs the smaller

def smaller_num(list_of_nums):
    # ''' 
    # list -> int

    # Outputs the smaller number in a list.

    # >>> smaller_num([1, 9, 94, 35, 26, 87])
    # 1

    # >>> smaller_num([12, 7, 23, 15, 9, 76])
    # 7
    # '''
 
    minimum = list_of_nums[0]
    for n in list_of_nums:
        if minimum > n:
            minimum = n

    
    return minimum

result = smaller_num([1, 9, 94, 35, 26, 87])
print(result)

