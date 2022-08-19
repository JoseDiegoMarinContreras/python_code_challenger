from tkinter.font import ROMAN


def int_to_roman(num: int) -> str:
    ROMAN_NUMS = {
        0: { 0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", },
        1: { 0: "", 1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC", },
        2: { 0: "", 1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM", },
        3: { 0: "", 1: "M", 2: "MM", 3: "MMM" },
    }

    return "%s%s%s%s"%(
                        ROMAN_NUMS[3][num//1000],
                        ROMAN_NUMS[2][(num%1000)//100],
                        ROMAN_NUMS[1][((num%1000)%100)//10],
                        ROMAN_NUMS[0][((num%100)%100)%10],
                      )
#III
num = 3
print(int_to_roman(num))

#LVIII
num = 58
print(int_to_roman(num))
#MCMXCIV
num = 1994
print(int_to_roman(num))