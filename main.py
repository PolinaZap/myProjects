print('Addition(+) = 1. Subtraction(-) = 2. Multiplication(*) = 3. Division(/) = 4. Exponentiation(**) = 5.')
z = int(input('Print the number of action you want to take:'))
if z > 5:
    print('Please, choose the action!')
if z < 1:
    print('Please, choose the action!')
if z == 1:
    a = int(input('Print the first addend:'))
    b = int(input('Print the second addend:'))
    print('The sum is', a + b, '.')
if z == 2:
    a = int(input('Print the minuend:'))
    b = int(input('Print the subtrahend:'))
    print('The difference is', a - b, '.')
if z == 3:
    a = int(input('Print the first multiplier:'))
    b = int(input('Print the second multiplier:'))
    print('The product is', a * b, '.')
if z == 4:
    a = int(input('Print the dividend:'))
    b = int(input('Print the divisor:'))
    if b > 0:
        print('The product is', a / b, '.')
    if b == 0:
        print('Division by zero is not possible.')
        r = int(input('Print a new divisor:'))
        if r == 0:
            print('You wrote zero again. Division by zero is not possible!')
        else:
            print('The product is', a / r, '.')
if z == 5:
    a = int(input('Print the first number:'))
    b = int(input('Print the second number:'))
    print('The answer is', a ** b, '.')
