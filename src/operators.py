class LogicOperator:

    def __init__(self):
        self.name = ''
    
    def eval(self, x, y):
        pass

class AND(LogicOperator):

    def __init__(self):
        self.name = "AND"
    
    def eval(self, x, y):
        return min(x, y)


class OR(LogicOperator):

    def __init__(self):
        self.name = "OR"
    
    def eval(self, x, y):
        return max(x, y)