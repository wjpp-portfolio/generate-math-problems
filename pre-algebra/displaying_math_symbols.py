import matplotlib.pyplot as plt
from fractions import Fraction
import math_lib
import random

MATPLOTLIB_OPERATOR_STRINGS = {
    '*': '\cdot',
    '/': '\div',
    '+': '+',
    '-': '-'
    }

include_negative_numbers = False
include_variables = False
include_decimal = False

class Fract:
    """fraction object which keeps track of non-simplified numerator and denominator"""
    def __init__(self, num, den):
        if num > den:
            num, den = den, num
        
        if num == den:
            num -= 1

        self.num = num
        self.den = den
        
    def as_string(self):
        """returns fraction string for use in matplotlib"""
        return '\\frac{{{0}}}{{{1}}}'.format(self.num, self.den)
    
class Fraction_Problem:
    """defines a construct to generate and solve fraction problems"""
    def __init__(self, number_of_fractions: int):
        self.equation_map = []
        for i in range(number_of_fractions):
            
            self.equation_map.append(Fract(random.randrange(1,10),random.randrange(2,20)))

            if i < number_of_fractions - 1:
                self.equation_map.append(random.choice(['+','-','*','/']))

    def solve(self):
        """evaluates fractions and operators"""
        char_code = 97
        string = ''
        for i in self.equation_map:
            if type(i) is Fract:
                string += chr(char_code)
                
                globals()['%s' % chr(char_code)] = Fraction(i.num, i.den)
                char_code += 1
            else:
                string += ' ' + i + ' '

        return eval(string)
        
    def show(self):
        string = ''
        for i in self.equation_map:
            if type(i) is Fract:
                string += i.as_string()
            else:
                string += MATPLOTLIB_OPERATOR_STRINGS[i]
            

        plt.plot()
        plt.text(0, 0, '$' + string + '$', fontsize=30)
        plt.show()

problem = Fraction_Problem(3)
problem.show()
