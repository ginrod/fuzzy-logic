class FuzzyInferenceSystem:
    def __init__(self, entry_variables, output_variable, rules):
        self.entry_variables = entry_variables
        self.output_variable = output_variable
        self.rules = rules
        self.consecuent_func = None
    
    def mamdani_method(self):
        rule_fuzzy_subset_funcs = []
        for rule in self.rules:
            vant = rule.antecedent.eval()
            func = lambda x: min(vant, rule.consecuence.membership_func(x))
            rule_fuzzy_subset_funcs.append(func)
        
        return lambda x: max([func(x) for func in rule_fuzzy_subset_funcs])
    
    def larsen_method(self):
        rule_fuzzy_subset_funcs = []
        for rule in self.rules:
            vant = rule.antecedent.eval()
            func = lambda x: vant * rule.consecuence.membership_func(x))
            rule_fuzzy_subset_funcs.append(func)
        
        return lambda x: max([func(x) for func in rule_fuzzy_subset_funcs])