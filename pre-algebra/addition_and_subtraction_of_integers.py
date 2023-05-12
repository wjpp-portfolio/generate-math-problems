

##OPERATORS = ['-','+']
##
##expression_list = []
##
##expression_list.append(str(random.randrange(-9,9)))
##for i in range(random.randrange(1,4)):
##    expression_list.append(random.choice(OPERATORS))
##    expression_list.append(str(random.randrange(-9,9)))
##
##
##expression = ''
##for item in expression_list:
##    if '-' in item and len(item) > 1:
##        item = '(' + item + ')'
##    if item == '-' or item == '+':
##        item = ' ' + item + ' '
##
##    expression += item
##
##
##print(expression)
##print(eval(expression))
import random

EXPONENTS = [2,3,4]
NUMBER_RANGE = 9

class Expression:
    """generates a maths expression based on given parameters"""
    def __init__(self,
                 number_range = NUMBER_RANGE,
                 include_addition = True,
                 include_subtraction = True,
                 include_multiplication = True,
                 include_division = True,
                 include_exponents = False,
                 include_variables = False
                 ):
        #addition, subtraction, multiplication, division

        self.expression = self.generate_expression()
        self.result = self.calculate_expression()

    def generate_expression(self):
        pass

    def calculate_expression(self):
        pass
    
a = Expression()
print(a.expression)
print(a.result)
