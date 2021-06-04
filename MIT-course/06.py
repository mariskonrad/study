# Write a for loop that sums the values 1 through end, inclusive. end is a variable that we define for you. 
# So, for example, if we define end to be 6, your code should print out the result:
# 21
# which is 1 + 2 + 3 + 4 + 5 + 6.

end = 6
s = 0
for num in range(0,end + 1):
    s = s + num
print(s)
