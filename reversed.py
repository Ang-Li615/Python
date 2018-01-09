class FloatRange():

    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        x = self.start
        while x <= self.end:
            yield x
            x = x + self.step

    def __reversed__(self):
        x = self.end
        while x >= self.start:
            yield x
            x = x - self.step



for k in FloatRange(1.0,6.0,0.5):
    print(k)

print('#'*20)

for k in reversed(FloatRange(1.0,6.0,0.5)):
    print(k)