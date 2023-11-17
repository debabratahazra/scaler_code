# print with gap 2,4,6,8,10, 12 ....
# print 1,3,7,13,....

n = int(input("Enter the end number: "))
gap = 0
prev_val = 1

while prev_val <= n:
    print(prev_val, end=" ")
    gap += 2
    prev_val += gap
