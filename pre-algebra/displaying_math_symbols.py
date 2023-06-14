import matplotlib.pyplot as plt
import math_lib
import random

MATPLOTLIB_OPERATOR_STRINGS = {
    0: '\cdot',
    1: '\div'
    }

class Fract:
    """defines a fraction object"""
    def __init__(self):
        num = random.randrange(1,21)
        den = random.randrange(1,21)
        
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
        self.fractions = []

        for i in range(number_of_fractions):
            self.fractions.append(Fract())

        
    def show(self):
        string = ''
        for i in self.fractions:
            string += i.as_string()
            if i != self.fractions[-1]:
                string += random.choice(MATPLOTLIB_OPERATOR_STRINGS)

        plt.plot()
        plt.text(0, 0, '$' + string + '$', fontsize=30)
        plt.show()

a = Fraction_Problem(2)
a.show()
