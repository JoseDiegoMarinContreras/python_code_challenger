"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.
"""

def isPalindrome(x: int) -> bool:
    s = str(x)
    return s == s[::-1]

#True
x = 12321
print(isPalindrome(x))

#False
x = -121
print(isPalindrome(x))

#False
x = 10
print(isPalindrome(x))