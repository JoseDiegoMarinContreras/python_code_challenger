def is_palindrome(s: str):
    return s == s[::-1]


val = "cbc"
print("'%s' - len: %s, is_palindrome: %s"%(val, len(val), is_palindrome(val)))

val = "ccbadeffedabcc"
print("'%s' - len: %s, is_palindrome: %s"%(val, len(val), is_palindrome(val)))