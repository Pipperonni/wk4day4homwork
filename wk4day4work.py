# In this Kata, you will be given a string and 
# your task will be to return a list of ints detailing the count of uppercase letters, 
# lowercase, numbers and special characters, as follows.

# O(n) There is only one loop and the rest are constants.
def num_char(string):
    char_count = []
    
    # O(1)
    digg = 0
    upp = 0
    low = 0
    spchar = 0
    # O(n)
    for char in string:
        # O(1)
        if char.isdigit():
            digg += 1
        elif char.isupper():
            upp += 1
        elif char.islower():
            low += 1
        else:
            spchar += 1
    
    # O(1)
    char_count.append(upp)
    char_count.append(low)
    char_count.append(digg)
    char_count.append(spchar)
    
    return char_count

st = "2R*h$h29NMe&"
print(num_char(st))


# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

# Example 1:
# a1 = ["arp", "live", "strong"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns ["arp", "live", "strong"]

# Example 2:
# a1 = ["tarp", "mice", "bull"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns []


a1 = ["arp", "strong", "live"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# O(n^2) There is a loop with in a loop.
def in_array(array1, array2):
    new_list = []
    # O(n)
    for a in array1:
        # O(n)
        for b in array2:
            # O(1)
            if a in b and a not in new_list:
                new_list.append(a)
    # O(1)
    new_list.sort()
    return new_list

print(in_array(a1,a2))

# Your task in this kata is to implement a function that calculates the sum of the integers inside a string. 
# For example, in the string 
# "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", 
# the sum of the integers is 3635.

import re

a = "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"

# O(n) This function is running once through a whole string.
def sum_of_integers_in_string(s):
    return sum(list(map(int, re.findall("\d+", s))))


print(sum_of_integers_in_string(a))
  
