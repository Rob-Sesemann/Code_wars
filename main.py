# Numerical Palindrome
# https://www.codewars.com/kata/58ba6fece3614ba7c200017f/train/python

def palindrome(num):
    num_str = str(num)
    if (type(num) != int) or num < 0:
        return "Not valid"
    elif num_str == num_str[::-1]: 
        return True
    else:
        return False









# Remove the occurances of an instance from one list in another
class List:
    def remove_(self, integer_list, values_list):
        integer_list = [i for i in integer_list if i not in values_list]
        return integer_list