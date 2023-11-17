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
