def double(n):
    return 2*n


print(double(10))

#############

ret = (lambda n: 2*n)(11)
print(ret)

############


def multi(n, m):
    return n*m


print(multi(10, 20))

##############

ret = (lambda n, m: n*m)(11, 10)
print(ret)
