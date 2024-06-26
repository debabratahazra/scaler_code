score = 2
if False:
    score = 66

def batting():
    if True:
        score = 40

batting()
print(score)

####################################

arr = [a+" "+b for a in [ "Hello", "Good"] for b in ["Dear", "Bye"]]
print(arr) 

########################

arr = [[1,2,3],[10,11,12],[4,5,6],[13,14,15],[10,1,2]]

print(max (arr, key=sum ) )

##############################

arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]

for i in range(0, 4):
  print(arr[i].pop(), end=" ")
print()

#####################################

list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
list2 = list1
list3 = list1[:]

list2[0] = 'Guava'
list3[1] = 'Kiwi'

total = 0
for ls in (list1, list2, list3):
  if ls[0] == 'Guava':
    total += 1

  if ls[1] == 'Kiwi':
    total += 20

print (total, list3[0])