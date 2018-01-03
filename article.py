import re #regular expression operation
from collections import Counter
TXT = open('sample.txt').read()  #TXT is a string
print TXT

L = re.split('\W+',TXT)
c = Counter(L)
print c.most_common(10)