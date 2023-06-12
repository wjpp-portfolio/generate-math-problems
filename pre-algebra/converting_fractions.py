import random



numerator = 0
denominator = random.randrange(5,50)

while numerator <= denominator:
    numerator = random.randrange(50,100)
print('Convert this improper faction to a mixed fraction, and simplify:')
print(numerator,'/', denominator)

a = numerator // denominator
p = denominator * a
n = numerator - p

candidates = []
for i in range(1, denominator):
    if n % i == 0 and denominator % i == 0:
        candidates.append(i)

answer = a, int(n / candidates[-1]),'/', int(denominator / candidates[-1])
