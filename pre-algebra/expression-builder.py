import random

MAX_NUMBER_OF_CONSTANTS = 1
MAX_RANGE_OF_CONSTANTS = 2

MAX_NUMBER_OF_VARIABLE_TERMS = 1
MAX_VARIABLE_VALUE = 9
COEFFICIENT_RANGE = 9

VARIABLES = ['a','b','c','x','y','z']

_in_use_variables = dict()

class Variable:
    """defines a mathmatical variable"""
    def __init__(self, value):
        self.value = value
        self.symbol = random.choice(list(
                                    set(VARIABLES) - set(_in_use_variables))
                                    )
        _in_use_variables[self.symbol] = self.value
        
class Term:
    """defines a single mathmatical term with various modifiers"""
    def __init__(self, value):
        self.variables = []
        self.coefficient = random.randrange(1,COEFFICIENT_RANGE)

        for i in range(random.randrange(0,MAX_NUMBER_OF_VARIABLE_TERMS+1)):
            self.variables.append(random.choice(VARIABLES))
              
    def show(self):
        output = str(self.coefficient)
        for i in self.variables:
            output += i

        print(output)

class Expression:
    """builds an expression with defined characteristics"""
    def __init__(self, value, number_of_terms):
        pass
    
a = Variable(6)

print(_in_use_variables)
