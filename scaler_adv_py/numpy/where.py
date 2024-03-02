import numpy as np

arr = np.arange(-3, 11)
print("arr value:", arr)
print("length", len(arr))

ret1 = np.where(arr > 4, 15, 20)
print("where with condition:", ret1)

ret2 = np.where(arr)
print("where without condition:", ret2)
