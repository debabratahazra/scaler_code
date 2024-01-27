import numpy as np

################################################################
print("1")
x = np.array([-5, 9, 20, 25, -3, 5, 16, 10, -8])
x[(x >= -5) & (x <= 15)] *= -1
print(x)


################################################################
print("2")

a = np.array([100, 200, 300, 400])

b = np.array([300, 200, 100, 400])

print(a == b)
##################################################
print("3")
start = -1  # start number
length = 10  # length of the array
step = 0.5

sequence = np.arange(start, start+(length*step), step)
print(sequence)
################################################################
print("4")
a = np.array(range(21)).reshape(7, -1)
print(a.ndim)
print(a.shape)
print(a[a > 7])
a[a > 7] = -1
print(a)
###################################
print("5")
arr = 2 * np.arange(0, 2, 0.5)
print(arr)

'''
if arr <= 0.6:          # Error
    print("condition satisfies")
else:
    print("condition doesn't satisfy") '''

################################################################
print("6")
x = np.array([[200, 200, 200], [300, 300, 300], [400, 400, 400]])
v = np.array([200, 300, 400])
print(v)
trans = v.T  # not transposing here for 1D array
print(trans)
print(v[:, None])   # kind of Transpose for 1D arrays
print(x / v[:, None])
print((x / v[:, None])[1][1])

########################################################################
print("7")
p = np.array([[0], [10], [20]])
print(p)
q = np.array([10, 11, 12])
print(q)
print()
print(p+q)
print((p + q)[1][1])
########################################################################
print("8")
a = np.array([[16, 5], [81, 6], [33, 1]])
print(a)
x = np.transpose(a).reshape(2, 3)
print(x)
print(x.flatten())
########################################################################
print("9")
a = np.array([[34, 28, 55], [8, 56, 3], [77, 87, 19]])
trans = a.transpose()
print(trans)
print(trans[-2, -2])

################################################################

print("10")
a = [[0,  1,  2,  3],
     [4,  5,  6,  7],
     [8,  9, 10, 11],
     [12, 13, 14, 15],
     [16, 17, 18, 19]]

narr = np.array(a)
print(narr)
print()
# 2D array slice
print(narr[2:4, :])
print()
print(narr[:, 1:3])
print()
print(narr[:, -1])
print()
print(narr[-1, :])
print()
print(narr[-2:, :])
################################################################
print("11")
a = np.array([[6, 28], [8, 56], [7, 19]])
x = np.transpose(a).reshape(1, 6)
print(x)
########################################################################
print("12")
x = np.ones((5, 5))
print(x)
x[1:-1, 1:-1] = 0
print(x)
########################################################################
print("13")
print(np.sort(np.array(['Ram', 'Astha', 'Raghavendra'])))
################################################################
print("14")
arr1 = np.array(['Ram', 'Astha', 'Brahat'])
arr2 = np.array(['Shyam', 'Kalyan', 'Naveen'])
print(arr1 > arr2)
################################################################
print("15")
arr = np.array([[2, 3, 4, 5], [1, 7, 3, 5], [2, 8, 6, 9], [11, 23, 12, 19]])
print(arr)
'''
Expectd output:
[[ 4  6  8 10]
 [ 2 14  6 10]
 [ 4 16 12 18]
 [22 46 24 38]]
 '''
# approach 1
arr1 = np.array([[2, 2, 2, 2]])


def func(x, y):
    return x * y


vec = np.vectorize(func)
print(vec(arr, arr1))
# approach 2
arr = np.array([[2, 3, 4, 5], [1, 7, 3, 5], [2, 8, 6, 9], [11, 23, 12, 19]])
print(arr)
arr1 = np.array([[2], [2], [2], [2]])


def func(x, y):
    return x * y


vec = np.vectorize(func)
print(vec(arr, arr1))
# approach 3
arr = np.array([[2, 3, 4, 5], [1, 7, 3, 5], [2, 8, 6, 9], [11, 23, 12, 19]])
print(arr)
arr1 = 2


def func(x, y):
    return x * y


vec = np.vectorize(func)
print(vec(arr, arr1))
########################################################################
print("16")
arr1 = np.array([1, 2, 3])
arr2 = np.array([9, 8, 7])
print("Multil 1\n", np.dot(arr1, arr2))

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1], [2]])
print("multi 2\n", np.dot(arr1, arr2))

arr1 = np.array([1, 2, 3])
k = 3
print("multi 3\n", np.dot(arr1, k))

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([1, 1])
print("multi 4\n", np.dot(arr1, arr2))
################################################################
print("17")
arr = np.arange(16).reshape(4, 4)
print(np.split(arr, 4))
############################################################
print("18")
a = np.array([[[0, 1, 2],
               [3, 4, 5],
               [6, 7, 8]],

              [[9, 10, 11],
               [12, 13, 14],
               [15, 16, 17]]])
print(a[1, :, :])
################################################################
# Deep copy and shallow copy
print("19")
arr = np.array([2, 4, 6, 8, 10])
c0 = arr
c0[0] = 12
print("arr", arr, "\nC0 = ", c0)
arr = np.array([2, 4, 6, 8, 10])
c1 = arr.view()
arr[0] = 12
print("arr", arr, "\nC1 = ", c1)
arr = np.array([2, 4, 6, 8, 10])
c2 = arr.copy()
arr[0] = 12
print("arr", arr, "\nC2 = ", c2)
################################################################
print("20")

arr = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])
print(np.hstack((arr, arr[:, [0]])))
################################################################
print("21")
arr = np.arange(10)
sp = np.split(arr, [5, 12])  # no error
print(sp)
################################################################
print("22")
# 3D array
arr = np.array([[[0, 1],
                 [2, 3]],

                [[4, 5],
                 [6, 7]]])
print(arr[:, 0:, :1])
