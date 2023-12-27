# (3 + 4) // 2 + 6  -> (7 // 2) + 6 -> 3 + 6 -> 9
import math
print((3 + 4) // 2 + 6)

print(True == 1)

""" val = input()
if val.lower() == "python":
    print("great choice!")
else:
    print("Think again?")


feedback = input()
if feedback == "":
    print("Feedback not provided")
elif feedback.lower() == "super" \
        or feedback.lower() == "great" \
        or feedback.lower() == "fantastic" or feedback.lower() == "awesome":
    print("Thank you so much!")
else:
    print("Thank you for providing the feedback") """


""" 
c = 0
while c <= 10:
    print(c)
    if c % 2:
        c -= 1
    else:
        c += 1 
        
        """

""" 
x = 2
for i in range(0, 4):
    if x % 2:
        x = x*2
    else:
        x = x+1


x = 1
for i in range(x):
    x = x+1
    print(i, end=" ")

x = 3.7
print(math.floor(x)) """


i = 0
if i == 0:
    pass
    print(i, end=" ")
i += 1
print(i, end=" ")
print()


i = 0
j = 0
while i <= 2:
    if j % 2:
        j += 1
    print(i, ":", j, end=" ")
    i += 1
    j += 1
print()


x = 13
y = 3
q = 0
r = 0
while x >= y:
    x -= y
    q += 1
print(q, x)


for i in range(1):
    for j in range(2):
        for k in range(1):
            print("a", end=" ")
        print(end="")
    print("c")


print(0 % 2)


n = 8
while n >= 0:
    n -= 2
    if n % 2 == 0:
        continue
    print(n, end=" ")
else:
    print("Exec", end=" ")


if True:
    print("Knock Knock")
if True:
    print("Who's There?")
if True:
    print("No One")


num = 6  # int(input("Enter value: "))
val = 0
for i in range(2, num):
    val = val + i
if val > 10:
    print('Hello, this is Raj')
else:
    print('There is no one')

x = 5
if x > 5:
    x = x*3
if x > 15:
    x = 0
print(x)


num = 2
while num > 1:
    num = num // 3
print(num)


a = [10, 20, 30, 440, 50, 60, 70, 80, 90, 100]

a[3:5]
a[:8]
a[:]
a[7:]
a[-2:-5:-1]
a[-2:-7]
a[:-5]
a[-2:]
a[-8:5]
a[-8:5:-1]

A = ["1", "2", "3", "4", "5", "6"]
A[len(A):] = ["7", "8"]
print(A)
A += ["9", "10"]
print(A)
A[-1:] = ["11", "12"]   # overwrite last element
print(A)

# ERROR here
# print("hello" + 1+2+3)

name_lst = ["Vijay", "Vickey"]
tup = ("Item_1", 0.5, name_lst)
name_lst.append("Vishal")
print(tup)


set1 = {1, 2, 4}
set2 = {4, 5, 6}
# print(len(set1 + set2))     # Error


sets = {3, 4, 5}
sets.update([1, 2, 3])
print(sets)


sets = {3, 4, 5}
# sets.add([1, 2, 3])  # error
print(sets)


d = {1: "one", 2: "two", 3: "three"}
for k, v in d.items():
    print(f"{k} --> {v}")
################################################################
s1 = "ab"
s2 = "cd"
s3 = ""

for i in range(len(s1)):
    for j in range(len(s2)):
        if i == j:
            s3 += s1[i] + s2[j]
        else:
            s3 += s2[j] + s1[i]

print(s3)
################################################################
x = 1
indicator_1 = True
indicator_2 = False

if indicator_1:
    indicator_1 = indicator_2
    indicator_2 = indicator_1
    if indicator_2:
        x = x - 1
    else:
        x = x / 1
print(x)
################
L = [1, 1, 1, 1, 1, 1, 1, 2]

print(L.count(L[0]) == len(L))
################################################################
