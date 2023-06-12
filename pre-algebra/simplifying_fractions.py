#This script generates composite numbers into fractions which can be simplified

import random

def composite_number():
    a = random.randrange(100) + 3
    counter = 0
    for i in range(1,a):
        if a%i == 0:
            counter += 1

    if counter > 2:
        return a 
    
    else:
        return a + 1


numerator = composite_number()
denominator = 0

while denominator <= numerator:
    denominator = composite_number()

print(numerator, '/', denominator)

candidates = []
for i in range(1, denominator):
    if numerator % i == 0 and denominator % i == 0:
        candidates.append(i)

simplified = int(numerator / candidates[-1]), '/', int(denominator / candidates[-1])
