class OperationObject:
    
    def eval(self):
        pass

class Value(OperationObject):

    def __init__(self, fuzzy_set, value=None):
        self.fuzzy_set = fuzzy_set
        self.value = value
    
    def eval(self):
        return fuzzy_set.membership_func(self.value)

class AND(OperationObject):

    def __init__(self, x, y):
        self.name = "AND"
        self.x = x
        self.y = y
    
    def eval(self):
        x, y = x.eval(), y.eval()
        return min(x, y)


class OR(OperationObject):

    def __init__(self, x, y):
        self.name = "OR"
        self.x = x
        self.y = y
    
    def eval(self):
        x, y = x.eval(), y.eval()
        return max(x, y)