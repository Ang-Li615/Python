import pickle
from random import randint
from collections import deque

N = randint(0,100)
# show recent 5 guess
history = deque([],5)

def guess(k):
    if k == N:
        print 'Right'
        return True
    elif k < N:
        print '%d is less than N' % k
    else:
        print '%d is larger than N' % k
    return False

while True:
    n = raw_input('Please input your number:\n')
    if n.isdigit():
        nn = int(n)
        history.append(nn)
        if guess(nn):
            break

    elif n == 'history?':
        print list(history)

pickle.dump(history,open('history','w'))   #save
h = list(pickle.load(open('history')))               #load
print h