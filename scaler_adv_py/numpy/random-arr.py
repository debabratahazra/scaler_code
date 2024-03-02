import numpy as np

arr = np.arange(0, 100)

i = len(arr)
while len(arr) > 0:
    index = np.random.randint(0, i)
    print(arr[index])
    i = i - 1
    arr = np.delete(arr, index)
print("done")
