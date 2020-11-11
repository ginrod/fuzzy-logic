class OperationObject:
    
    def eval(self):
        pass

class Value(OperationObject):

    def __init__(self, fuzzy_set, value=None):
        self.fuzzy_set = fuzzy_set
        self.value = value
    
    def eval(self):
        return self.fuzzy_set.membership_func(self.value)

class AND(OperationObject):

    def __init__(self, x, y):
        self.name = "AND"
        self.x = x
        self.y = y
    
    def eval(self):
        x, y = self.x.eval(), self.y.eval()
        return min(x, y)


class OR(OperationObject):

    def __init__(self, x, y):
        self.name = "OR"
        self.x = x
        self.y = y
    
    def eval(self):
        x, y = self.x.eval(), self.y.eval()
        return max(x, y)

class MinOperator:
    def __init__(self, vant, function):
        self.vant = vant
        self.function = function
    
    def eval(self, x):
        return min(self.vant, self.function(x))

class ProductOperator:
    def __init__(self, vant, function):
        self.vant = vant
        self.function = function
    
    def eval(self, x):
        return self.vant * self.function(x)

class MaxOperator:
    def __init__(self, functions):
        self.functions = functions
    
    def eval(self, x):
        return max([func.eval(x) for func in self.functions])