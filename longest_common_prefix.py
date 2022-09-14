"""
A function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

def longest_common_prefix(strs: list[str] ) -> str:
    strs.sort()
    i = 0
    for s in strs[0]:
        if strs[-1][i] == s:
            i += 1
        else:
            break
    return strs[0][:i]


# fl
value = ["flower","flow","flight"]
print(longest_common_prefix(value))

# ""
value = ["dog","racecar","car"]
print(longest_common_prefix(value))