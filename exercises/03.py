# create a program that receives a list of numbers and outputs the greater

def greater_num(list_of_nums):
    # ''' 
    # list -> int

    # Outputs the greater number in a list.

    # >>> greater_num([1, 9, 94, 35, 26, 87])
    # 87

    # >>> greater_num([12, 7, 23, 15, 9, 76])
    # 76
    # '''
 
    maximum = list_of_nums[0]
    for n in list_of_nums:
        if maximum < n:
            maximum = n

    
    return maximum

result = greater_num([1, 9, 94, 35, 26, 87])
print(result)

