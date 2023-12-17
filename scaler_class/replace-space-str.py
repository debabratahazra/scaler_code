s = "This is a string"

str1 = ""
for ch in s:
    if ch.isspace():
        str1 += "_"
    else:
        str1 += ch

print(str1)
