from random import randint
data = []
for i in range(10):
    data.append(randint(-10,10))

print data

s = set(data)
snew = ([x for x in s if x%3==0])
print snew