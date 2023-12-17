s = "this is a string for count characters"

d = {}

set_s = set(s)  # get the all unique char from string

for ch in set_s:
    # string count() returns the total count of characters of that string
    d[ch] = s.count(ch)
print(d)
