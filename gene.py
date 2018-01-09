class PrimeNumbers():

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNumber(self, k):
        print('isPrimeNumber')
        if k in range(0,2):
            return False

        for i in range(2, k):
            if k % i == 0:
                return False
                break

        return True

    def __iter__(self):
        print('iter')
        for k in range(self.start,self.end+1):
            if self.isPrimeNumber(k):
                yield k


for x in PrimeNumbers(1,100):
    print(x)

