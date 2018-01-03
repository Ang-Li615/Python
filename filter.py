import timeit
L = [1,2,6,18,-7,29,3,-10]
#def f(x):
#    if x >= 0:
#        return True
#
#Lrest = filter(f,L)
#print Lrest


Lrest = filter(lambda x: x>=0, L)
print Lrest


Lnew = [x for x in L if x >= 0]
print Lnew