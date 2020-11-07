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
        return -10000 <= x and x <= -1000 and (1000 + x) / (1000 - 10000)  or 0

    @staticmethod
    def few_negative(x):
        return -1000 <= x and x <= -10 and (10 + x) / (10 - 1000)  or 0

    @staticmethod
    def negligible(x):
        return -10 <= x and x <= 0 and (10 + x) / 10 or 0
        
    @staticmethod
    def positive(x):
        return 0 <= x and x <= 10000 and (10000 - (10000 - x)) / 10000 or 0
    
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