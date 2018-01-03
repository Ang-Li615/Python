from random import randint
from time import time
from collections import OrderedDict

players = list('ABCDEFGH')
print players
d = OrderedDict()
start = time()

for i in range(len(players)):
    raw_input()
    p = players.pop(randint(0,len(players)-1))
    end = time()
    print i+1, p, end - start
    d[p] = (i+1, end - start)

print
print '-'*20
for key in d:
    print key, d[key]
