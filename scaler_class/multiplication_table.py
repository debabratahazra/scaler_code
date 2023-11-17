n = int(input("Enter number for table:"))

for i in range(1, n+1):
    for j in range(1, 11):
        print(i*j, end=" ")
    print()
