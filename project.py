import statistics
import numpy as np

class Project:
    def __init__(self, data):
        self.data = data
        self.mean = 0
        self.med = 0
        self.max = 0
        self.min = 0
        self.std = 0
        self.pop_std = 0
        self.percentile1 = 0
        self.percentile3 = 0
        self.result = {}

    def median(self):
        self.med = statistics.median(self.data)
        self.result.update({'mediana': self.med})

    def standart_deviation(self):
        self.std = statistics.stdev(self.data)
        self.result.update({'std': self.std})

    def population_std(self):
        list1 = []
        self.average()
        for i in range(len(self.data)):
            list1.append(pow((self.data[i]-self.mean), 2))
        self.pop_std = pow(sum(list1)/len(data), 1/2)
        self.result.update({'population std': self.pop_std})

    def percentile(self):
        self.percentile1 = np.percentile(data, 25)
        self.percentile3 = np.percentile(data, 75)
        self.result.update({'percentile 1': self.percentile1, 'percentile3': self.percentile3})

    def maxmin(self):
        self.max = max(data)
        self.min = min(data)
        self.result.update({'max': self.max, 'min': self.min})

    def average(self):
        self.mean = sum(data)/len(data)
        self.result.update({'mean': self.mean})

    def get_data(self):
        self.median()
        self.standart_deviation()
        self.population_std()
        self.percentile()
        self.maxmin()
        self.average()
        for key, values in self.result.items():
            print ('{}: {}'.format(key, values))

data = [1_320_900, 370_000, 10_175_000]
data.sort()
pro = Project(data).get_data()
