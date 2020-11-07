class LinguisticVariable:
    def __init__(self, name, domain, categories=[]):
        self.name = name
        self.domain = domain
        self.categories = categories

class FuzzySet:
    def __init__(self, name, domain, linguistic_variable_name, membership_func):
        self.name = name
        self.membership_func = membership_func
        self.linguistic_variable_name = linguistic_variable_name