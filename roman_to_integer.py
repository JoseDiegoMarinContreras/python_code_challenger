from tkinter.font import ROMAN


def int_to_roman(num: int) -> str:
    ROMAN_NUMS = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }
    roman = ""

    for s in ROMAN_NUMS:
        roman += ROMAN_NUMS[s] * (num // s)
        num %= s

    return roman

#III
num = 3
print(int_to_roman(num))

#LVIII
num = 58
print(int_to_roman(num))
#MCMXCIV
num = 1994
print(int_to_roman(num))