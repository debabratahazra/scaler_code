s = "This is STRING"

for i in range(len(s)):
    if s[i] >= "A" and s[i] <= "Z":
        s = s.replace(s[i], chr(ord(s[i]) + 32))
print(s)
