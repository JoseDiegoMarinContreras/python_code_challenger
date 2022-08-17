"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.
"""

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    
    x2 = 0
    aux_x = x
    while(aux_x > 0):
        x2 *= 10
        x2 += aux_x%10
        aux_x //= 10

    return x == x2

#True
x = 12321
print(isPalindrome(x))

#False
x = -121
print(isPalindrome(x))

#False
x = 10
print(isPalindrome(x))