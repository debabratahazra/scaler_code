def maxOnes(arr):
    # write code
    pass
    maxOnes = -1
    index = -1
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                count += 1
        if maxOnes < count:
            maxOnes = count
            index = i
    return index


arr = [[0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 1, 1]]
ret = maxOnes(arr)
print(ret)
