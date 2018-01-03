d = {}

d['Jim'] = (1, 39)
d['Tian'] = (2, 40)
d['Letitia'] = (3,45)

for key in d:
    print key

from collections import OrderedDict
d = OrderedDict()
d['Jim'] = (1, 39)
d['Tian'] = (2, 40)
d['Letitia'] = (3,45)

for key in d:
    print key
