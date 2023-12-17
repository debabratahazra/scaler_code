
arr1 = [1, 2, 3]
arr2 = [6, 5, 4]

arr1.append(arr2)
print("append: ", arr1)


arr1 = [1, 2, 3]
arr2 = [6, 5, 4]

arr1.extend(arr2)
print("extend: ", arr1)


arr1 = [1, 2, 3]
arr2 = [6, 5, 4]

arr1.sort(reverse=False)
print("sort: ", arr1)


arr1 = [1, 2, 3]
arr1.remove(2)
print("after remove 2: ", arr1)


arr1 = [1, 2, 3]
arr1.clear()
print("after clear ", arr1)


arr1 = [1, 2, 3, 2, 1, 2, 2, 3, 1]
countVal = arr1.count(2)
print("count 2: ", countVal)


arr1 = [1, 5, 6, 7, 2, 3, 4]
indexVal = arr1.index(2)
print("index of value 2 ", indexVal)


arr1 = [1, 4, 5, 8, 2, 1, 9, 2, 3]
val = arr1.pop(2)
print("index 2 pop value: ", val)
print("after pop arr is: ", arr1)
