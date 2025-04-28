import sys
print(sys.platform)
print(2**100)   # 2^100
x = 'Spam!'
print(x * 10)
print("hello" + " " + "world")

y = 'Not Spam!'
z = 'All Spam!'


# List Comprehension ###################################

list_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
selected_values = [x for x in list_values if x < 6]
print(selected_values)
# Output: [1, 2, 3, 4, 5]

# List Comprehension with Conditionals
selected_values_2 = [x < 5 for x in list_values]
print(selected_values_2)
# Output: [True, True, True, False, False, False, False, False, False, False]