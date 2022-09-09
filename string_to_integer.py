"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit
signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

  1. Read in and ignore any leading whitespace.
  2. Check if the next character (if not already at the end of the string) is
     '-' or '+'. Read this character in if it is either. This determines if the
     final result is negative or positive respectively. Assume the result is
     positive if neither is present.
  3. Read in next the characters until the next non-digit character or the end
     of the input is reached. The rest of the string is ignored.
  4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If
     no digits were read, then the integer is 0. Change the sign as necessary
     (from step 2).
  5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
     then clamp the integer so that it remains in the range. Specifically,
     integers less than -231 should be clamped to -231, and integers greater
     than 231 - 1 should be clamped to 231 - 1.
  6. Return the integer as the final result.

Note:
   - Only the space character ' ' is considered a whitespace character.
   - Do not ignore any characters other than the leading whitespace or the
     rest of the string after the digits.
"""


def my_atoi(s: str): 
    s = s.lstrip()
    digits = { "0", "1", "2", "3",
                    "4", "5", "6",
                    "7", "8", "9", }
    signs = { "+", "-", }
    num_s = ""
    sign = ""
    for char in s:
        if char in signs:
            if sign or num_s:
                break
            sign = char
        elif char in digits:
            num_s += char
        else:
            break
        
    INT_MIN = -2**31
    INT_MAX = -1*INT_MIN - 1
    num = int(sign + num_s) if num_s else 0
    return num \
           if INT_MIN < num < INT_MAX\
           else (
           INT_MIN
           if INT_MIN >= num
           else INT_MAX)
    
# 42
val = "42"
print(my_atoi(val))

# -42
val = "   -42"
print(my_atoi(val))

# 4193
val = "4193 with words"
print(my_atoi(val))

# 0
val = "words and 987"
print(my_atoi(val))

# 1
val = "+1"
print(my_atoi(val))

# 0
val = "00000-42a1234"
print(my_atoi(val))

# -2147483648
val = "-2147483648"
print(my_atoi(val))

# 0
val = "  +  413"
print(my_atoi(val))