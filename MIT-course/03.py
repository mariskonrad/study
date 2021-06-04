# Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you. 
# So, for example, if we define end to be 6, your code should print out the result:
# 21
# which is 1 + 2 + 3 + 4 + 5 + 6.

end = 6
num = 0
s = 0
while num < end:
    num += 1
    s = s + num
print(s)
