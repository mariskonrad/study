# Assume s is a string of lower case characters.
#  Write a program that prints the number of times the string 'bob' occurs in s.
#  For example, if s = 'azcbobobegghakl', then your program should print
#  Number of times bob occurs is: 2

num_words = 0
s = 'azcbobobegghakl'
for chunk in range(len(s)):
    if s[chunk: chunk + 3] == "bob":
        num_words += 1
print(num_words)

