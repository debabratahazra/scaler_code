a = "101010101"
b = "1010101110aabb"


# Note: {"1","0"} == {"0","1"}  , order not matter in Set
s = set(b)
if s == {"0", "1"} or s == {"0"} or s == {"1"}:
    print("Binary")
else:
    print("Not Binary")
