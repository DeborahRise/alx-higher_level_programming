#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    val1 = 0

    rom_num = {
            'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
            'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
            'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
            'M': 1000
            }
    for n in range(len(roman_string)):
        if roman_string[n] not in rom_num:
            return 0
        if n != (len(roman_string) - 1) and \
                rom_num[roman_string[n]] < rom_num[roman_string[n + 1]]:
            val1 += rom_num[roman_string[n]] * -1
        else:
            val1 += rom_num[roman_string[n]]
    return val1
