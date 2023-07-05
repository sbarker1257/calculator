operand = input('op pls')

x = int(input('x'))
y = int(input('y'))



operander= ['+','-','*','/']

print(operander.index(operand))

i = operander.index(operand)

print(operander[i])

if i == 0:
    result = x + y
    print(result)
elif i == 1:
    result = x - y
    print(result)
elif i == 2:
    result = x * y
    print(result)
elif i == 3:
    result = x / y
    print(result)