# create a program that receives a list of numbers and outputs the position of the smaller

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
    # position = 0
    for n in range(list_of_nums):
        if minimum > list_of_nums[n]:
            minimum = n
    
    return minimum
    

# result = smaller_num([9, 1, 94, 35, 26, 87])
# print(result)


for n in range(10):
    print(n)
