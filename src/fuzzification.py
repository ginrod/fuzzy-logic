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
        elif -10000 <= x and x <= -100: return (100 + x) / (100 - 10000)
        # if x > -100
        return 0

    @staticmethod
    def few_negative(x):
        if x < -1000: return 1
        elif -1000 <= x and x <= -5: return (5 + x) / (5 - 1000)
        # if x > -5
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
        rank = func.__name__ == 'very_negative' and (-10000, -100) or \
               func.__name__ == 'few_negative' and (-1000, -5) or \
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
        if 500 <= x and x <= 4750: return (4750 - 500 - (4750 - x)) / (4750 - 500)
        elif 4750 < x and x <= 10000: return (10000 - x) / (10000 - 4750)
        # if x < 500 or x > 10000
        return 0
    
    @staticmethod
    def high(x):
        if x < 5000: return 0
        elif 5000 <= x and x <= 25000: return (25000 - 5000 - (25000 - x)) / (25000 - 5000)
        # if x > 25000
        return 1

    @staticmethod
    def plot(func):
        rank = func.__name__ == 'few' and (0, 1000) or \
               func.__name__ == 'medium' and (500, 10000) or \
               func.__name__ == 'high' and (5000, 25000)
        
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
        if x < 0: return 1
        elif 0 <= x and x <= 1500: return (1500 - x) / 1500
        # if x > 1500
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
        elif 10000 <= x and x <= 25000: return (25000 - 10000 - (25000 - x)) / (25000 - 10000)
        # if x > 25000
        return 1

    @staticmethod
    def plot(func):
        rank = func.__name__ == 'very_few' and (0, 10) or \
               func.__name__ == 'few' and (0, 1500) or \
               func.__name__ == 'medium' and (1000, 10000) or \
               func.__name__ == 'high' and (10000, 25000)
        
        general_plot(func, rank)

# Sales.plot(Sales.very_few)
# Sales.plot(Sales.few)
# Sales.plot(Sales.medium)
# Sales.plot(Sales.high)