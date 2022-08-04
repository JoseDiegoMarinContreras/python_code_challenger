def length_of_longest_substring(s: str) -> int:
    indexes = {}
    start_index = 0
    length_substring = 0
    
    for i in range(len(s)):
        char_s = s[i]
        if char_s in indexes and indexes[char_s] >= start_index:
            start_index = indexes[char_s] + 1

        length_substring = max(length_substring, i - start_index + 1)
        indexes[char_s] = i
    
    return length_substring
#2
s = "abba"
print(length_of_longest_substring(s))
#3
s = "abcabcbb"
print(length_of_longest_substring(s))