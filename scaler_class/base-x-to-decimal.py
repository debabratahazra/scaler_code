def baseX_to_decimal(number, base):
    decimal = 0
    power = 0
    while number > 0:
        digit = number % 10
        decimal += digit * (base ** power)
        number //= 10
        power += 1
    return decimal


# here 21 is itself of base 3, o/p will be in base 10 value
print(baseX_to_decimal(21, 3))
