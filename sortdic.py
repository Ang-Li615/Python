from random import randint

d = {k:randint(60,100) for k in range(10)}
print d


#L = []
#for k,v in d.items():
#    L.append((v,k))

# Using zip
L = zip(d.values(),d.keys())

print L
LL = sorted(L)
print LL