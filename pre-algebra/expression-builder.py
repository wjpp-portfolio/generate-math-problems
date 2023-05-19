import random

MAX_NUMBER_OF_CONSTANTS = 1
MAX_RANGE_OF_CONSTANTS = 2

MAX_NUMBER_OF_VARIABLE_TERMS = 1
MAX_VARIABLE_VALUE = 5
MAX_COEFFICIENT_RANGE = 5

VARIABLE_SYMBOLS = ['a','b','c','x','y','z']

_in_use_variables = dict()

EXPRESSION_LAYOUTS = {
    1: ['var_t'],
    2: ['const_t'],
    3: ['var_t', 'const_t'],
    4: ['var_t', 'const_t', 'var_t']
    }

class Variable:
    """defines a mathmatical variable"""
    def __init__(self, value):
        self.value = value
        self.symbol = random.choice(list(
                                    set(VARIABLE_SYMBOLS) - set(_in_use_variables))
                                    )
        _in_use_variables[self.symbol] = self.value
        
class Term:
    """defines a single mathmatical term as either a constant term or variable term (coefficient + variable)"""
    def __init__(self, term_type, value):

        self.math_value = value #real integer value used for calculations, not display
        self.term_type = term_type
        getattr(self, term_type)(value)
            
        
        
        
    def constant(self, value):
        """as a constant this just returns the passed value and is defined as a funciton for program consistency"""
        self.constant = value
    
    def variable(self, value):
        """creates a variable and coefficient which together give product of 'value'"""
        integers = []

        for i in range(1,value+1):

            if value%i == 0:
                integers.append(i)
   
        if len(integers) > 1:
            integers.remove(1)


        self.variable = Variable(random.choice(integers))
        self.coefficient = int(value/self.variable.value)

        assert self.variable.value * self.coefficient == value
        
    def display(self):
        if self.term_type == 'constant':
            return self.constant
        else:
            return str(self.coefficient) + str(self.variable.symbol)
        

class Expression:
    """builds an expression with defined characteristics"""
    def __init__(self, value):
        self.expression_terms = []
        chosen_expression_layout_key = random.choice(list(EXPRESSION_LAYOUTS))

        for i in EXPRESSION_LAYOUTS[chosen_expression_layout_key]:
            self.expression_terms.append(getattr(self,i)())
            
    def var_t(self):
        return Term('variable',random.randrange(MAX_COEFFICIENT_RANGE+1))


    def const_t(self):
        return Term('constant',random.randrange(MAX_VARIABLE_VALUE+1))

b = Expression(20)
for i in b.expression_terms:
    print(i.display())
