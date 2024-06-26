# Remove duplicate tuples from list of tuples
arr= [(1,2),(2,3),(2,3),(1,2),(5,6)]
ret = [ item for item in set (tuple(i) for i in arr )]
print(ret)

arr= [(1,2),(2,3),(2,3),(1,2),(5,6)]
ret = [ (a,b) for i, [a,b] in enumerate(arr) if not any ((d==b and a==c) for c, d in arr[ : i])]
print(ret)


arr= [(1,2),(2,3),(2,3),(1,2),(5,6)]
ret = list (set ( [ i for i in arr ]))
print(ret)

###########################################################

