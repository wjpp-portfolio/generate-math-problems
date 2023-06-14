#This script generates composite numbers into fractions which can be simplified

import random
import math_lib

number_pool = math_lib.gen_multiplication_table(90,12) + math_lib.gen_prime_number_list(90)
sorted(list(set(number_pool)))

common_factor_candidates = []

while len(list(set(common_factor_candidates))) < 5:
    common_factor_candidates = []
    numerator = int(random.choice(number_pool) / 2)
    denominator = 0

    while denominator <= numerator:
        denominator = random.choice(number_pool)
        
    for i in range(1, denominator):
        if numerator % i == 0 and denominator % i == 0:
            common_factor_candidates.append(i)


print('Simplify this fraction:')
print(numerator, '/', denominator)
answer = int(numerator / common_factor_candidates[-1]), '/', int(denominator / common_factor_candidates[-1])

