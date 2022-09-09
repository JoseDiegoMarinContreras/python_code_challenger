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