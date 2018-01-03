from random import randint, sample

s1 = {k:randint(1,4) for k in sample('abcdefg',randint(3,6))}
print s1

s2 = {k:randint(1,4) for k in sample('abcdefg',randint(3,6))}
print s2

s3 = {k:randint(1,4) for k in sample('abcdefg',randint(3,6))}
print s3

############
# iterate
#res = []
#for k in s1:
#    if k in s2 and k in s3:
#        res.append(k)
#print res
############


############
#intersect of set
#s4 = set(s1.keys()) & set(s2.keys()) & set(s3.keys())
#print s4
############


############
#s4 = s1.viewkeys() & s2.viewkeys() & s3.viewkeys()
#print s4
###########


###########
#map + reduce
s4 = map(dict.viewkeys,[s1,s2,s3])
print s4

s5 = reduce(lambda x,y: x & y, s4)
print s5
############