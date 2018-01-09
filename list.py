# How to obtain the first 3 most frequent number in a list

from random import randint

L = [randint(0,20) for _ in range(30)]
print L


d = dict.fromkeys(L, 0)

for x in L:
    d[x] = d[x]+1

print d

# Another method is using collections.Counter
from collections import Counter
c2 = Counter(L)    #c2 is also a dictionary just like d
c3 = c2.most_common(3)

Lval = []
for v in d.values():
    Lval.append(v)

Lval = sorted(Lval,reverse=-1)
print Lval
Lval = set(Lval)
print Lval
LL = []
for x in Lval:
    LL.append(x)

LL = sorted(LL,reverse=-1)
print LL

dnew = {}
for n in range(len(LL)):
    if len(dnew) < 3:
        for k,v in d.items():
            if v == LL[n]:
                dnew[k] = v

print dnew