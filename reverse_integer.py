"""
Given a signed 32-bit integer x, return x with its digits reversed. If
reversing x causes the value to go outside the signed 32-bit integer range
[-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers
(signed or unsigned).
"""

def reverse(x: int) -> int:
    s = str(x)
    s = s[0] + s[:0:-1] if x < 0 else s[::-1]
    num = int(s)
    return num if -2**31 < num < 2**31 -1 else 0

# 321
val = 123
print(reverse(val))

# -321
val = -123
print(reverse(val))

# 12
val = 120
print(reverse(val))