f = open('a.txt')

from itertools import islice
for line in islice(f,2,5):
    print(line)