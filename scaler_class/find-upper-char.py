s = "This is RANDOM string"

count = 0
for ch in s:
    if ord(ch) >= 65 and ord(ch) <= 90:
        count += 1
print(count)
