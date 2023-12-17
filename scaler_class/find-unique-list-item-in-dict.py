# In the dict, the value are LIST, find the whose key has more unique values within the each list

d = {"scaler": [5, 7, 5, 4, 5], "is": [6, 7, 4, 3, 3], "best": [9, 9, 6, 5, 5]}
# ans is "is" as it has more unique values
key = ""
max_unique_values = float('-inf')
for k, v in d.items():
    v_set = set(v)
    if max_unique_values < len(v_set):
        key = k
        max_unique_values = len(v_set)

print(key)
