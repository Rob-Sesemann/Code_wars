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
    