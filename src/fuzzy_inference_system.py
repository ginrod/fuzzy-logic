import numpy as np
from operators import MinOperator, ProductOperator, MaxOperator

class FuzzyInferenceSystem:
    def __init__(self, entry_variables, output_variable, rules):
        self.entry_variables = entry_variables
        self.output_variable = output_variable
        self.rules = rules
    
    def mamdani_method(self):
        rule_fuzzy_subset_funcs = []
        for rule in self.rules:
            vant = rule.antecedent.eval()
            # func = lambda x: min(vant, rule.consecuence.membership_func(x))
            func = MinOperator(vant, rule.consecuence.membership_func)
            rule_fuzzy_subset_funcs.append(func)
        
        # return lambda x: max([func(x) for func in rule_fuzzy_subset_funcs])
        return MaxOperator(rule_fuzzy_subset_funcs)
    
    def larsen_method(self):
        rule_fuzzy_subset_funcs = []
        for rule in self.rules:
            vant = rule.antecedent.eval()
            # func = lambda x: vant * rule.consecuence.membership_func(x)
            func = ProductOperator(vant, rule.consecuence.membership_func)
            rule_fuzzy_subset_funcs.append(func)
        
        # return lambda x: max([func(x) for func in rule_fuzzy_subset_funcs])
        return MaxOperator(rule_fuzzy_subset_funcs)
    
    def COA(self, ruled_fuzzy_set_func, domain=None):
        inf, sup = domain or self.output_variable.domain

        num, dem = 0, 0
        for zj in np.arange(inf, sup + 1, 1):
            miu_zj = ruled_fuzzy_set_func.eval(zj)
            num += miu_zj * zj
            dem += miu_zj
        
        return dem and num / dem or (inf + sup) / 2
    
    # Mean of Maximum
    def MOM(self, ruled_fuzzy_set_func, domain=None):
        inf, sup = domain or self.output_variable.domain

        vmax = max(ruled_fuzzy_set_func.eval(zj) for zj in np.arange(inf, sup + 1, 1))
        zj_with_vmax = []
        for zj in np.arange(inf, sup + 1, 1):
            if ruled_fuzzy_set_func.eval(zj) == vmax:
                zj_with_vmax.append(zj) 

        return sum(zj_with_vmax) / len(zj_with_vmax)