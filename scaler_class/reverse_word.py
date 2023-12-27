s = "i.like.this.program.very.much"
s_split = s.split(".")
new_str = ""
for index in range(len(s_split)-1, -1, -1):
    new_str += s_split[index]+"."
print(new_str.rstrip("."))
