# one dict is there, one keys[] is define. Based on keys, need to fetch only remaining ley:value from dict

d = {
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5"
}

keys = [2, 3]

new_d = {k: d[k] for k in d.keys() if k not in keys}
print(new_d)    # remaining key-value pairs will print
