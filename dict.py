#import random
#d = {k : random.randint(60,100) for k in range(1,21)}
#print d

from random import randint
d = {k: randint(60,100) for k in range (1,20)}
print d

dnew = {k:v for k,v in d.items() if v>= 90}
print dnew