import math as m
import numpy as np
from scipy.integrate import trapz
import matplotlib.pyplot as plt
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
    
    def BOA(self, ruled_fuzzy_set_func, domain=None):
        def _integrate(f, a, b, dx = 1):
            y = [f(x) for x in np.arange(a, b, dx)]

            return trapz(y, dx=dx)
        
        inf, sup = domain or self.output_variable.domain

        left, right = inf, sup
        mid = 0.0
        iteration_number = 0

        while abs(right - left) > 0  and iteration_number <= 15:
            mid = (left + right) / 2

            suml = _integrate(ruled_fuzzy_set_func.eval, inf, mid)
            sumr = _integrate(ruled_fuzzy_set_func.eval, mid, sup)

            right = suml >= sumr and mid or right
            left = suml < sumr and mid or left

            iteration_number += 1

        return mid