print('Addition = +. Subtraction = -. Multiplication = *. Division = /. Exponentiation = **.')
z = str(input('Print the number of action you want to take:'))
if z != '+' and  z != '-' and z != '*' and z != '/' and z != '**':
    print('Please, choose the action!')
if z == '+':
    a = int(input('Print the first addend:'))
    b = int(input('Print the second addend:'))
    print('The sum is', a + b, '.')
if z == '-':
    a = int(input('Print the minuend:'))
    b = int(input('Print the subtrahend:'))
    print('The difference is', a - b, '.')
if z == '*':
    a = int(input('Print the first multiplier:'))
    b = int(input('Print the second multiplier:'))
    print('The product is', a * b, '.')
if z == '/':
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
if z == '**':
    a = int(input('Print the first number:'))
    b = int(input('Print the second number:'))
    print('The answer is', a ** b, '.')
