def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def longest_palindrome(s: str) -> str:
        if is_palindrome(s):
            return s
        
        if len(s) < 3:
            return s[0]

        l_i = start = 0
        size = 1

        for i in range(1, len(s) + 1):
            l_i = i - size

            s1, s2 = s[l_i-1 : i], s[l_i : i]

            if len(s1) >= size and is_palindrome(s1):
                start, size = l_i - 1, size + 2
            elif len(s2) >= size and is_palindrome(s2):
                start, size = l_i, size + 1

        return s[start:start+size-1]

# bcddcb
val = "abcddcb"
print(longest_palindrome(val))

# a
val = "a"
print(longest_palindrome(val))

# bb
val = "cbbd"
print(longest_palindrome(val))

# bab
val = "babad"
print(longest_palindrome(val))

# cc
val = "ccd"
print(longest_palindrome(val))