def is_palindrome(val):
    return val == val[::-1]

val = "13031"
print(is_palindrome(val))

val = "1331"
print(is_palindrome(val))

val = "46380"
print(is_palindrome(val))
