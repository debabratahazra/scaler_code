import numpy as np

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(type(a))
narr = np.array(a)
print(type(narr))

'''
Expected output:

[[7 4 1]
 [8 5 2]
 [9 6 3]]
 
'''
narr = narr.T   # Transpose -> Row to Column and Column to Row
print(narr)
narr = narr[:, ::-1]    # Take all rows, column part just reversed
print(narr)
