import random

EXPONENTS = [2,3,4]
EXPONENT_FREQUENCY = 0.1
VARIABLES = ['a','b','c']
VARIABLE_FREQUENCY = 0.1
INTEGER_RANGE = 9
MAX_NUMBER_OF_TERMS = 5 

class Operand:
    #has mathematical value e.g. 5
    #has printed value e.g. x
    def __replace_with_variable(self):
        pass
    def __invert_integer(self):
        pass
    def __add_brackets(self):
        pass
    def __add_exponent(self):
        pass
    
class Expression:
    """generates a maths expression based on given parameters"""
    def __init__(self,
                 integer_range = INTEGER_RANGE,
                 include_addition = True,
                 include_subtraction = True,
                 include_multiplication = True,
                 include_division = False,
                 include_exponents = False,
                 include_variables = False
                 ):
        
        self.operator_pool = []
        if include_addition == True:
            self.operator_pool.append('+')
        if include_subtraction == True:
            self.operator_pool.append('-')
        if include_multiplication == True:
            self.operator_pool.append('*')
        if include_division == True:
            self.operator_pool.append('/')

        self.include_exponents = include_exponents
        self.include_variables = include_variables
                 
        self.expression = self.generate_expression()
        self.result = self.calculate_expression()

    def generate_expression(self):
        """builds a string of operands and operators that can be passed to eval() function"""
        exp = ''
        exp += self.__generate_operand()
        for term in range(random.randrange(1, MAX_NUMBER_OF_TERMS - 1)):

            exp = exp + ' ' + self.__generate_operator()
            exp = exp + ' ' + self.__generate_operand()

        return exp
    
    def calculate_expression(self):
        """evaluates expression"""
        return eval(self.expression)

    def __generate_operand(self):
        """generates a random interger between INTERGER_RANGE and its negative equivalent"""
        return self.__add_exponents(self.__add_parentheses(random.randrange(-INTEGER_RANGE, INTEGER_RANGE)))
    
    def __generate_operator(self):
        """selects a random operator from the operator_pool as built during class init"""
        return random.choice(self.operator_pool)

    def __add_parentheses(self, operand):
        """adds parenthese to negative integers. all integers (negative or otherwise) are cast to string. parenthese are added for reading clarify and to differentiate from subtraction operator"""
        if operand >= 0:
            return str(operand)
        else:
            return '(' + str(operand) + ')'

        
    def __add_exponents(self,operand):
        """adds an expontent to an operand based on the EXPONENT_FREQUENCY"""
        if self.include_exponents == True and random.random() <= EXPONENT_FREQUENCY:
            return operand + '**' + str(random.choice(EXPONENTS))
        else:
            return operand

    def __replace_with_variable(self,operand):
        """replaces an interger operand with a variable; will occure based on the VARIABLE_FREQUENCY. Inclusion of variables will display variables key"""
        if self.include_variables == True and random.random() <= VARIABLE_FREQUENCY:
            pass
        

a = Expression(include_variables = True)
print(a.expression)
print(a.result)
