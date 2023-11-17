
num = int(input())
total = 0

while num > 0:
    reminder = num % 10
    total += reminder
    num = num // 10

print(total)
