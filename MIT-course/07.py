# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', your program should print:
#  Number of vowels: 5

num_vowels = 0
s = 'azcbobobegghakl'
for vowel in s:
    if vowel == "a" or vowel == "e" or vowel == "i" \
    or vowel == "o" or vowel == "u":
        num_vowels += 1
print("Number of vowels is:", num_vowels)
