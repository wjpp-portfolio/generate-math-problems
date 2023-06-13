#This script generates composite numbers into fractions which can be simplified

import random
import math_lib



numerator = math_lib.generate_composite_number(100)
denominator = 0

while denominator <= numerator:
    denominator = math_lib.generate_composite_number(100)
print('Simplify this fraction:')
print(numerator, '/', denominator)

candidates = []
for i in range(1, denominator):
    if numerator % i == 0 and denominator % i == 0:
        candidates.append(i)

answer = int(numerator / candidates[-1]), '/', int(denominator / candidates[-1])
