s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
#res = s.split(';')
#for x in list(map(lambda x : x.split('|'),res)):
#    print(x)

def mySplit(s,ds):
    res = [s]
    for d in ds:
        t = []
        map(lambda x: t.extend(x.split(d)),res)
        res = t

    return res

print(mySplit(s,';,|\t'))

