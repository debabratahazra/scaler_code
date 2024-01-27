def roman_to_int(s):
    rom_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    int_val = 0
    for i in range(len(s)):
        print(rom_val[s[i]], rom_val[s[i - 1]])
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            print(int_val, rom_val[s[i]], 2 * rom_val[s[i - 1]],
                  rom_val[s[i]] - 2 * rom_val[s[i - 1]])
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            print(int_val, rom_val[s[i]])
            int_val += rom_val[s[i]]
    print(int_val)
    return int_val


print(roman_to_int('III'))   # Output: 3
print(roman_to_int('IV'))    # Output: 4
print(roman_to_int('IX'))    # Output: 9
print(roman_to_int('LVIII'))  # Output: 58
print(roman_to_int('MCMXCIV'))  # Output: 1994
