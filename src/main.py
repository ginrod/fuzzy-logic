from operators import *
from fuzzy_entities import *
from fuzzification import Fluctuation, Purchases, Sales
from fuzzy_inference_system import FuzzyInferenceSystem
from random import randrange, randint

def define_fluctuation():
    categories = { 
        'very_negative': { 'rank': (-10000, -1000), 'miu': Fluctuation.very_negative }, 
        'few_negative':  { 'rank': (-1000, -10),    'miu': Fluctuation.few_negative }, 
        'negligible':    { 'rank': (-10, 0),        'miu': Fluctuation.negligible }, 
        'positive':      { 'rank': (0, 10000),      'miu': Fluctuation.positive } 
    }
    fluctuation = LinguisticVariable('fluctuation', (-10000, 10000), categories)
    very_negative = FuzzySet('very_negative', fluctuation.categories['very_negative']['rank'], 
                        fluctuation.categories['very_negative']['miu'], 'fluctuation')
    few_negative = FuzzySet('few_negative', fluctuation.categories['few_negative']['rank'], 
                        fluctuation.categories['few_negative']['miu'], 'fluctuation')
    negligible = FuzzySet('negligible', fluctuation.categories['negligible']['rank'], 
                    fluctuation.categories['negligible']['miu'], 'fluctuation')
    positive = FuzzySet('positive', fluctuation.categories['positive']['rank'], 
                    fluctuation.categories['positive']['miu'], 'fluctuation')
    
    return fluctuation, [very_negative, few_negative, negligible, positive]

def define_purchases():
    categories = { 
        'few':    { 'rank': (0, 1000),      'miu': Purchases.few }, 
        'medium': { 'rank': (1000, 10000),  'miu': Purchases.medium }, 
        'high':   { 'rank': (10000, 50000), 'miu': Purchases.high } 
    }
    purchases = LinguisticVariable('purchases', (0, 50000), categories)
    few = FuzzySet('few', purchases.categories['few']['rank'], purchases.categories['few']['miu'], 'purchases')
    medium = FuzzySet('medium', purchases.categories['medium']['rank'], purchases.categories['medium']['miu'], 'purchases')
    high = FuzzySet('high', purchases.categories['high']['rank'], purchases.categories['high']['miu'], 'purchases')
    
    return purchases, [few, medium, high]

def define_sales():
    categories = { 
        'very_few': { 'rank': (0, 10),        'miu': Sales.very_few }, 
        'few':      { 'rank': (10, 1000),     'miu': Sales.few }, 
        'medium':   { 'rank': (1000, 10000),  'miu': Sales.medium }, 
        'high':     { 'rank': (10000, 50000), 'miu': Sales.high } 
    }
    sales = LinguisticVariable('sales', (0, 50000), categories)
    very_few = FuzzySet('very_few', sales.categories['very_few']['rank'], sales.categories['very_few']['miu'], 'sales')
    few = FuzzySet('few', sales.categories['few']['rank'], sales.categories['few']['miu'], 'sales')
    medium = FuzzySet('medium', sales.categories['medium']['rank'], sales.categories['medium']['miu'], 'sales')
    high = FuzzySet('high', sales.categories['high']['rank'], sales.categories['high']['miu'], 'sales')
    
    return sales, [very_few, few, medium, high]

def define_rules(variables, sets, vfluctuation, vpurchases):
    rules = []

    # Define first rule: if fluctuation is positive then sales is high
    antecedent = Value(sets['fluctuation']['positive'], vfluctuation)
    consequence = sets['sales']['high']
    
    rule = FuzzyRule(variables, sets, antecedent, consequence)
    rules.append(rule)

    # Define second rule: if fluctuation is negligible and (purchases is medium or purchases is high) then sales is medium
    purchases_is_high = Value(sets['purchases']['high'], vpurchases)
    purchases_is_medium = Value(sets['purchases']['medium'], vpurchases)
    fluctuation_is_negligible = Value(sets['fluctuation']['negligible'], vfluctuation)

    antecedent = AND(fluctuation_is_negligible, OR(purchases_is_medium, purchases_is_high))
    consequence = sets['sales']['medium']
    
    rule = FuzzyRule(variables, sets, antecedent, consequence)
    rules.append(rule)
    
    # Define third rule: if fluctuation is very negative and then sales is very few
    antecedent = Value(sets['fluctuation']['very_negative'], vfluctuation)
    consequence = sets['sales']['very_few']
    
    rule = FuzzyRule(variables, sets, antecedent, consequence)
    rules.append(rule)

    # Define fourth rule: if fluctuation is few negative and purchases is few then sales is few
    fluctuation_is_few_negative = Value(sets['fluctuation']['few_negative'], vfluctuation)
    purchases_is_few = Value(sets['purchases']['few'], vpurchases)

    antecedent = AND(fluctuation_is_few_negative, purchases_is_few)
    consequence = sets['sales']['few']

    rule = FuzzyRule(variables, sets, antecedent, consequence)
    rules.append(rule)

    return rules

def test_mamdani_COA(variables, sets, vfluctuation, vpurchases):
    rules = define_rules(variables, sets, vfluctuation, vpurchases)
    FIS = FuzzyInferenceSystem([variables['fluctuation'], variables['purchases']], variables['sales'], rules)
    defuzzied_output = FIS.COA(FIS.mamdani_method())
    
    return defuzzied_output

def test_mamdani_BOA(variables, sets, vfluctuation, vpurchases):
    rules = define_rules(variables, sets, vfluctuation, vpurchases)
    FIS = FuzzyInferenceSystem([variables['fluctuation'], variables['purchases']], variables['sales'], rules)
    defuzzied_output = FIS.BOA(FIS.mamdani_method())
    
    return defuzzied_output

def test_mamdani_MOM(variables, sets, vfluctuation, vpurchases):
    rules = define_rules(variables, sets, vfluctuation, vpurchases)
    FIS = FuzzyInferenceSystem([variables['fluctuation'], variables['purchases']], variables['sales'], rules)
    defuzzied_output = FIS.MOM(FIS.mamdani_method())
    
    return defuzzied_output

def test_larsen_COA(variables, sets, vfluctuation, vpurchases):
    rules = define_rules(variables, sets, vfluctuation, vpurchases)
    FIS = FuzzyInferenceSystem([variables['fluctuation'], variables['purchases']], variables['sales'], rules)
    defuzzied_output = FIS.COA(FIS.larsen_method())
    
    return defuzzied_output

def test_larsen_BOA(variables, sets, vfluctuation, vpurchases):
    rules = define_rules(variables, sets, vfluctuation, vpurchases)
    FIS = FuzzyInferenceSystem([variables['fluctuation'], variables['purchases']], variables['sales'], rules)
    defuzzied_output = FIS.BOA(FIS.larsen_method())
    
    return defuzzied_output

def test_larsen_MOM(variables, sets, vfluctuation, vpurchases):
    rules = define_rules(variables, sets, vfluctuation, vpurchases)
    FIS = FuzzyInferenceSystem([variables['fluctuation'], variables['purchases']], variables['sales'], rules)
    defuzzied_output = FIS.MOM(FIS.larsen_method())
    
    return defuzzied_output

def execute_set_of_tests(variables, sets, fluctuation_values, purchases_values):
    for vfluctuation, vpurchases in zip(fluctuation_values, purchases_values):
        print(f"\nFluctuation={vfluctuation}")
        print(f"Purchases={vpurchases}")

        print("\nExecuting FIS using Mamdani and COA")
        output = test_mamdani_COA(variables, sets, vfluctuation, vpurchases)
        print(output)

        print("\nExecuting FIS using Mamdani and BOA")
        output = test_mamdani_BOA(variables, sets, vfluctuation, vpurchases)
        print(output)

        print("\nExecuting FIS using Mamdani and MOM")
        output = test_mamdani_MOM(variables, sets, vfluctuation, vpurchases)
        print(output)

        print("\nExecuting FIS using Larsen and COA")
        output = test_larsen_COA(variables, sets, vfluctuation, vpurchases)
        print(output)

        print("\nExecuting FIS using Larsen and BOA")
        output = test_larsen_BOA(variables, sets, vfluctuation, vpurchases)
        print(output)

        print("\nExecuting FIS using Larsen and MOM")
        output = test_larsen_MOM(variables, sets, vfluctuation, vpurchases)
        print(output)

if __name__ == '__main__':
    fluctuation_var, fluctuation_sets = define_fluctuation()
    purchases_var, purchases_sets = define_purchases()
    sales_var, sales_sets = define_sales()

    variables = { 'fluctuation': fluctuation_var, 'purchases': purchases_var, 'sales': sales_var }
    sets = { 'fluctuation': {}, 'purchases': {}, 'sales': {} }
    for fset in fluctuation_sets + purchases_sets + sales_sets:
        sets[fset.linguistic_variable_name][fset.name] = fset
    
    # Testing rules with some values

    # First set of testing
    fluctuation_positive = [50, 500, 5000]
    purchases_any = [randrange(0, 25000), randrange(0, 25000), randrange(0, 25000)]
    # It should output a value corresponding with high Sales
    print("Testing first set: fluctuation positive and random purchases")
    execute_set_of_tests(variables, sets, fluctuation_positive, purchases_any)


    # Second set of testing
    fluctuation_negligible = [-10, -5, 0]
    purchases_medium = [1000, 5000, 8000]
    purchases_high = [10000, 15000, 20000]
    purchases = [p[randint(0, 1)] for p in zip(purchases_medium, purchases_high)]
    # It should output a value corresponding with medium Sales
    print("\nTesting second set: fluctuation negligible and medium or high purchases")
    execute_set_of_tests(variables, sets, fluctuation_negligible, purchases)


    # Third set of testing
    fluctuation_very_negative = [-5000, -1000, -100]
    purchases_any = [randrange(0, 25000), randrange(0, 25000), randrange(0, 25000)]
    # It should output a value corresponding with very few Sales
    print("\nTesting third set: fluctuation very negative and random purchases")
    execute_set_of_tests(variables, sets, fluctuation_very_negative, purchases_any)


    # Fourth set of testing
    fluctuation_very_few = [-50, -100, -10]
    purchases_few = [10, 100, 500]
    # It should output a value corresponding with few Sales
    print("\nTesting fourth set: fluctuation very few and few purchases")
    execute_set_of_tests(variables, sets, fluctuation_very_few, purchases_few)