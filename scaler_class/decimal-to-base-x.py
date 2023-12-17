def decimal_to_baseX(decimal_num, base):
    if decimal_num == 0:
        return '0'
    digits = []
    while decimal_num:
        decimal_num, remainder = divmod(decimal_num, base)
        digits.append(str(remainder))
    return ''.join(digits[::-1])


# here sending decimal value and returning int of base 3 value
# here 7 is base 10, o/p is base 3 value
print(decimal_to_baseX(7, 3))
