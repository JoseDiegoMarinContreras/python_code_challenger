"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows
like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
"""

def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    i, step = 0, 1
    zigzag_map = numRows*[""]
    for char in s:
        zigzag_map[i] += char
        step = 1 if i == 0 else -1 if i == numRows-1 else step
        i += step

    return "".join(zigzag_map)
        
# PAYPALISHIRING
val = "PAYPALISHIRING"
print(convert(val, 1))

# PYAIHRNAPLSIIG
print(convert(val, 2) == "PYAIHRNAPLSIIG")

# PAHNAPLSIIGYIR
print(convert(val, 3) == "PAHNAPLSIIGYIR")

# PINALSIGYAHRPI
print(convert(val, 4) == "PINALSIGYAHRPI")

# PHASIYIRPLIGAN
print(convert(val, 5) == "PHASIYIRPLIGAN")