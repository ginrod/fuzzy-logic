import matplotlib.pyplot as plt
import numpy as np

def general_plot(f, interval, step=0.01, label=None):
    x = np.arange(interval[0], interval[1], step)
    y = [f(k) for k in x]

    plt.plot(x, y, label=label)
    plt.show()

class Fluctuation:
    
    @staticmethod
    def very_negative(x):
        if x < -10000: return 1
        elif -10000 <= x and x <= -1000: return (1000 + x) / (1000 - 10000)
        # if x > -1000
        return 0

    @staticmethod
    def few_negative(x):
        if x < -1000: return 1
        elif -1000 <= x and x <= -10: return (10 + x) / (10 - 1000)
        # if x > -10
        return 0

    @staticmethod
    def negligible(x):
        if x < -10: return 0
        elif -10 <= x and x <= 0: return (10 + x) / 10
        # if x > 0
        return 1

    @staticmethod
    def positive(x):
        if x < 0: return 0
        elif 0 <= x and x <= 10000: return (10000 - (10000 - x)) / 10000
        # if x > 10000
        return 1
    
    @staticmethod
    def plot(func):
        rank = func.__name__ == 'very_negative' and (-10000, -1000) or \
               func.__name__ == 'few_negative' and (-1000, -10) or \
               func.__name__ == 'negligible' and (-10, 0) or \
               func.__name__ == 'positive' and (0, 10000)
        
        general_plot(func, rank)

# Fluctuation.plot(Fluctuation.very_negative)
# Fluctuation.plot(Fluctuation.few_negative)
# Fluctuation.plot(Fluctuation.negligible)
# Fluctuation.plot(Fluctuation.positive)

class Purchases:
    
    @staticmethod
    def few(x):
        if x < 0: return 1
        elif 0 <= x and x <= 1000: return (1000 - x) / 1000
        # if x > 1000
        return 0

    @staticmethod
    def medium(x):
        if 1000 <= x and x <= 4500: return (4500 - 1000 - (4500 - x)) / (4500 - 1000)
        elif 4500 < x and x <= 10000: return (10000 - x) / (10000 - 4500)
        # if x < 1000 or x > 10000
        return 0
    
    @staticmethod
    def high(x):
        if x < 10000: return 0
        elif 10000 <= x and x <= 50000: return (50000 - 10000 - (50000 - x)) / (50000 - 10000)
        # if x > 50000
        return 1

    @staticmethod
    def plot(func):
        rank = func.__name__ == 'few' and (0, 1000) or \
               func.__name__ == 'medium' and (1000, 10000) or \
               func.__name__ == 'high' and (10000, 50000)
        
        general_plot(func, rank)

# Purchases.plot(Purchases.few)
# Purchases.plot(Purchases.medium)
# Purchases.plot(Purchases.high)

class Sales:
    
    @staticmethod
    def very_few(x):
        if x < 0: return 1
        elif 0 <= x and x <= 10: return (10 - x) / 10
        # if x > 10
        return 0

    @staticmethod
    def few(x):
        if x < 10: return 1
        elif 10 <= x and x <= 1000: return (1000 - 10 - (1000 - x)) / (1000 - 10)
        # if x > 1000
        return 0

    @staticmethod
    def medium(x):
        if 1000 <= x and x <= 4500: return (4500 - 1000 - (4500 - x)) / (4500 - 1000)
        elif 4500 < x and x <= 10000: return (10000 - x) / (10000 - 4500)
        # if x < 1000 or x > 10000
        return 0
    
    @staticmethod
    def high(x):
        if x < 10000: return 0
        elif 10000 <= x and x <= 50000: return (50000 - 10000 - (50000 - x)) / (50000 - 10000)
        # if x > 50000
        return 1

    @staticmethod
    def plot(func):
        rank = func.__name__ == 'very_few' and (0, 10) or \
               func.__name__ == 'few' and (10, 1000) or \
               func.__name__ == 'medium' and (1000, 10000) or \
               func.__name__ == 'high' and (10000, 50000)
        
        general_plot(func, rank)

# Sales.plot(Sales.very_few)
# Sales.plot(Sales.few)
# Sales.plot(Sales.medium)
# Sales.plot(Sales.high)