from operators import *
from fuzzy_entities import *
from fuzzification import Fluctuation, Purchases, Sales

def define_fluctuation():
    categories = { 
        'very_negative': { 'rank': (-10000, -1000), 'miu': Fluctuation.very_negative }, 
        'few_negative':  { 'rank': (-1000, -10),    'miu': Fluctuation.few_negative }, 
        'negligible':    { 'rank': (-10, 0),        'miu': Fluctuation.negligible }, 
        'positive':      { 'rank': (0, 10000),      'miu': Fluctuation.positive } 
    }
    fluctuation = LinguisticVariable('fluctuation', (-10000, 10000), categories)
    very_negative = FuzzySet('very_negative', 'fluctuation', 
                        fluctuation.categories['very_negative']['rank'], fluctuation.categories['very_negative']['miu'])
    few_negative = FuzzySet('few_negative', 'fluctuation', 
                        fluctuation.categories['few_negative']['rank'], fluctuation.categories['few_negative']['miu'])
    negligible = FuzzySet('negligible', 'fluctuation', 
                        fluctuation.categories['negligible']['rank'], fluctuation.categories['negligible']['miu'])
    positive = FuzzySet('positive', 'fluctuation', 
                        fluctuation.categories['positive']['rank'], fluctuation.categories['positive']['miu'])
    
    return fluctuation, [very_negative, few_negative, negligible, positive]

def define_purchases():
    categories = { 
        'few':    { 'rank': (0, 1000),      'miu': Purchases.few }, 
        'medium': { 'rank': (1000, 10000),  'miu': Purchases.medium }, 
        'high':   { 'rank': (10000, 50000), 'miu': Purchases.high } 
    }
    purchases = LinguisticVariable('purchases', (0, 50000), categories)
    few = FuzzySet('few', 'purchases', purchases.categories['few']['rank'], purchases.categories['few']['miu'])
    medium = FuzzySet('medium', 'purchases', purchases.categories['medium']['rank'], purchases.categories['medium']['miu'])
    high = FuzzySet('high', 'purchases', purchases.categories['high']['rank'], purchases.categories['high']['miu'])
    
    return purchases, [few, medium, high]

def define_sales():
    categories = { 
        'very_few': { 'rank': (0, 10),        'miu': Sales.very_few }, 
        'few':      { 'rank': (10, 1000),     'miu': Sales.few }, 
        'medium':   { 'rank': (1000, 10000),  'miu': Sales.medium }, 
        'high':     { 'rank': (10000, 50000), 'miu': Sales.high } 
    }
    sales = LinguisticVariable('sales', (0, 50000), categories)
    very_few = FuzzySet('very_few', 'sales', sales.categories['very_few']['rank'], sales.categories['very_few']['miu'])
    few = FuzzySet('few', 'sales', sales.categories['few']['rank'], sales.categories['few']['miu'])
    medium = FuzzySet('medium', 'sales', sales.categories['medium']['rank'], sales.categories['medium']['miu'])
    high = FuzzySet('high', 'sales', sales.categories['high']['rank'], sales.categories['high']['miu'])
    
    return sales, [very_few, few, medium, high]

if __name__ == '__main__':
    fluctuation_var, fluctuation_sets = define_fluctuation()
    purchases_var, purchases_sets = define_purchases()
    sales_var, sales_sets = define_sales()