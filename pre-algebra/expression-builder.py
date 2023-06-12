import random


EXPRESSION_LAYOUTS = {
    1: ['var_t', 'const_t'],
    2: ['const_t', 'var_t'],
    3: ['bracket_t', 'const_t'],
    4: ['var_t', 'const_t', 'var_t'],
    5: ['const_t', 'var_t', 'const_t'],
    6: ['bracket_t'],
    7: ['var_t', 'bracket_t']
    }

MAX_VARIABLE_VALUE = 5
MAX_COEFFICIENT_RANGE = 5

VARIABLE_SYMBOLS = ['a']
OPERANDS = ['+', '-', '*', '/']

_in_use_variables = dict()


##class Term:
##    """defines a single mathmatical term as either a constant term or variable term (coefficient + variable)"""
##    def __init__(self, term_type, value):
##
##        self.math_value = value #real integer value used for calculations, not display
##        self.term_type = term_type
##        getattr(self, term_type)(value)
##            
##        
##        
##        
##    def constant(self, value):
##        """as a constant this just returns the passed value and is defined as a funciton for program consistency"""
##        self.constant = value
##    
##    def variable(self, value):
##        """creates a variable and coefficient which together give product of 'value'"""
##        integers = []
##
##        for i in range(1,value+1):
##
##            if value%i == 0:
##                integers.append(i)
##   
##        if len(integers) > 1:
##            integers.remove(1)
##
##
##        self.variable = Variable(random.choice(integers))
##        self.coefficient = int(value/self.variable.value)
##
##        assert self.variable.value * self.coefficient == value
##        
##    def display(self):
##        if self.term_type == 'constant':
##            return self.constant
##        else:
##            return str(self.coefficient) + str(self.variable.symbol)
##        
##


class Expression:
    """builds an expression with defined characteristics"""
    def __init__(self):
        self.expression_terms = []
        chosen_expression_layout_key = random.choice(list(EXPRESSION_LAYOUTS))

        for i in EXPRESSION_LAYOUTS[chosen_expression_layout_key]:
            self.expression_terms.append(getattr(self,i)())
            self.expression_terms.append(OPERANDS[random.choice([0,1])])

        del self.expression_terms[-1]
    def var_t(self):
        coefficient = random.choice([2,3,4,5])
        random.choice(VARIABLE_SYMBOLS)
        return str(coefficient) + random.choice(VARIABLE_SYMBOLS)
        #return Term('variable',random.randrange(MAX_COEFFICIENT_RANGE+1))

    def const_t(self):
        #return Term('constant',random.randrange(MAX_VARIABLE_VALUE+1))
        return random.randrange(MAX_VARIABLE_VALUE+1) + 2
    
    def bracket_t(self):
        
        bracket_terms = []
        for i in EXPRESSION_LAYOUTS[random.choice([1,2])]:
            bracket_terms.append(getattr(self,i)())

        return str(random.randrange(MAX_VARIABLE_VALUE+1) + 2) + '(' + str(bracket_terms[0]) + ' ' + OPERANDS[random.choice([0,1])] + ' ' + str(bracket_terms[1]) + ')'
        #return Term('bracket',random.randrange(MAX_VARIABLE_VALUE+1))

exp1 = Expression()
exp2 = Expression()
for i in exp1.expression_terms:
    print(str(i) + ' ', end='')
    
print('= ', end='')

for i in exp2.expression_terms:
    print(str(i) + ' ', end='')
