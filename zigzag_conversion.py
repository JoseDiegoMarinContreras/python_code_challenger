from functools import reduce
def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    s_index = 0
    zigzag_map = [[] for r in range(numRows)]
    col_num = 0
    zigzag_interval = numRows - 2

    while s_index < len(s):
        for i in range(numRows):
            if col_num == 0 and s_index < len(s):
                zigzag_map[i].append(s[s_index])
                s_index += 1
            elif i == zigzag_interval and s_index < len(s):
                zigzag_map[i].append(s[s_index])
                s_index += 1
                zigzag_interval -= 1

            

        col_num += 1
        if col_num == numRows - 1:
            zigzag_interval = numRows - 2
            col_num = 0

    zigzag_map = reduce(lambda a,b: a+b, zigzag_map)
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

a = [
["P", "", "", "I", "",  "", "N",],
["A", "", "L", "S", "", "I", "G",],
["Y", "A", "", "H", "R", "", "",],
["P", "", "", "I", "", "",  "",],]