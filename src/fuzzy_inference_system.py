class FuzzyInferenceSystem:
    def __init__(self, entry_variables, output_variable, rules):
        self.entry_variables = entry_variables
        self.output_variable = output_variable
        self.rules = rules