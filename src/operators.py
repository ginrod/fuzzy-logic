class OperationObject:
    
    def eval(self, x, y):
        pass

class Value(OperationObject):

    def __init__(self, value):
        self.value = value
    
    def eval(self):
        return self.value

class LogicOperator(OperationObject):

    def __init__(self):
        self.name = ''
    
    def eval(self, x, y):
        pass

class AND(LogicOperator):

    def __init__(self):
        self.name = "AND"
    
    def eval(self, x, y):
        x, y = x.eval(), y.eval()
        return min(x, y)


class OR(LogicOperator):

    def __init__(self):
        self.name = "OR"
    
    def eval(self, x, y):
        x, y = x.eval(), y.eval()
        return max(x, y)