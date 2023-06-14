import matplotlib.pyplot as plt
import random

MATPLOTLIB_OPERATOR_STRINGS = {
    0: '\cdot',
    1: '\div'
    }

def gen_fraction():
    """returns fraction string for use in matplotlib"""
    num = random.randrange(1,21)
    den = random.randrange(1,21)
    
    if num > den:
        num, den = den, num
        
    if num == den:
        num -= 1
        
    return '\\frac{{{0}}}{{{1}}}'.format(num, den)

printable_problem = '$' + gen_fraction() + random.choice(MATPLOTLIB_OPERATOR_STRINGS) + gen_fraction() + '$'
print(printable_problem)

plt.plot()
plt.text(0, 0, printable_problem, fontsize=30)
plt.show()
