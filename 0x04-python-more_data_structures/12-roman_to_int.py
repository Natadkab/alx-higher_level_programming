#!/usr/bin/python3
def to_sub(ls):
    max_ls = max(ls)
    to_sub_num = 0

    for n in ls:
        if max_ls > n:
            to_sub_num += n

    return max_ls - to_sub_num


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0

    rom_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    rom_key_list = list(rom_dict.keys())

    num = 0
    last_rom = 0
    list_num = [0]
    for ch in roman_string:
        for r_num in rom_key_list:
            if ch == r_num:
                if rom_dict.get(ch) <= last_rom:
                    num += to_sub(list_num)
                    list_num = [rom_dict.get(ch)]
                else:
                    list_num.append(rom_dict.get(ch))

                last_rom = rom_dict.get(ch)

    num += to_sub(list_num)
    return num
