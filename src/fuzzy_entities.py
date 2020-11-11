class LinguisticVariable:
    def __init__(self, name, domain, categories={}):
        self.name = name
        self.domain = domain
        self.categories = categories

class FuzzySet:
    def __init__(self, name, domain, membership_func, linguistic_variable_name):
        self.name = name
        self.domain = domain
        self.membership_func = membership_func
        self.linguistic_variable_name = linguistic_variable_name

class FuzzyRule:
    def __init__(self, variables, sets, antecedent, consecuence):
        self.variables = variables
        self.sets = sets
        self.antecedent = antecedent
        self.consecuence = consecuence