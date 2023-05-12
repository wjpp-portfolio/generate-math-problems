import random

OPERATORS = ['-','+']

expression_list = []

expression_list.append(str(random.randrange(-9,9)))
for i in range(random.randrange(1,4)):
    expression_list.append(random.choice(OPERATORS))
    expression_list.append(str(random.randrange(-9,9)))


expression = ''
for item in expression_list:
    if '-' in item and len(item) > 1:
        item = '(' + item + ')'
    if item == '-' or item == '+':
        item = ' ' + item + ' '

    expression += item


print(expression)
print(eval(expression))
