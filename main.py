import math

class Dataset:
    def __init__(self):
        self.data = []
        self.median = 0
        self.mean = 0
        self.range = 0
        self.variance = []
        self.standardDeviation = 0

        self.add()
        self.stats()
        
    def add(self):
        while(True):
            num = int((input("Input numbers or -1 to quit: ")))
            if(num == -1):
                break
            self.data.append(num)

    def findMedian(self):
        self.data = sorted(self.data)
        length = len(self.data) 
        mid = int(length / 2)
        if(length % 2 == 1):
            self.median = self.data[mid]
        else:
            self.median = (self.data[mid] + self.data[mid - 1]) / 2

    def findMean(self):
        for i in self.data:
            self.mean += i
        self.mean = self.mean / len(self.data)
        
    def findRange(self):
        self.data = sorted(self.data)
        self.range = self.data[-1] - self.data[0]

    def findVariance(self):
        for i in self.data:
            self.variance.append((i - self.mean) ** 2)

        temp = 0
        for i in self.variance:
            temp += i

        temp = temp / (len(self.variance) - 1)
        self.variance = temp

    def findStandardDeviation(self):
        self.standardDeviation = math.sqrt(self.variance)

    def stats(self):
        self.findMedian()
        self.findMean()
        self.findRange()
        self.findVariance()
        self.findStandardDeviation()

        print(f'Array: {self.data}')
        print(f'Median: {self.median}')
        print(f'Range: {self.range}')
        print(f'Mean: {self.mean}')
        print(f'Variance: {self.variance}')
        print(f'Standard Deviation: {self.standardDeviation}')

if __name__ == "__main__":
  work = Dataset()
  
