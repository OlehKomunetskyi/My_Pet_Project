import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "You cannot divide by zero"
    return x / y


def calculate_percentage(x, percentage):
    return x * (percentage / 100)


def calculate_square_root(x):
    return math.sqrt(x)


def calculate_exponentiation(x, exponent):
    return x ** exponent


def calculator():
    print(' --Simple calculator--')
    print('Please choose an option :')
    print('1. Add +')
    print('2. Subtract -')
    print('3. Multiply *')
    print('4. Divide */*')
    print('5. Percentage %')
    print('6. Square Root')
    print('7. Exponentiation')


if __name__ == '__main__':
    calculator()
    while True:
        choice: str = input('Enter the option number (type "exit" to quit):\n')

        if choice.lower() == 'exit':
            print('OK, bye!')
            break

        if choice not in ['1', '2', '3', '4', '5', '6', '7']:
            print('Choose a number from 1 to 7')
            continue

        if choice == '1':
            try:
                num1 = float(input('Enter the first number:\n'))
                num2 = float(input('Enter the second number:\n'))
                result = add(num1, num2)
                print(f'the result of {num1} + {num2} = {result}.')
            except ValueError:
                print('*Enter a number!*\n')

        elif choice == '2':
            try:
                num1 = float(input('Enter the first number:\n'))
                num2 = float(input('Enter the second number:\n'))
                result = subtract(num1, num2)
                print(f'the result of {num1} - {num2} = {result}.')
            except ValueError:
                print('*Enter a number!*')

        elif choice == '3':
            try:
                num1 = float(input('Enter the first number:\n'))
                num2 = float(input('Enter the second number:\n'))
                result = multiply(num1,  num2)
                print(f'the result of {num1} * {num2} = {result}.')
            except ValueError:
                print('*Enter a number!*')

        elif choice == '4':
            try:
                num1 = float(input('Enter the first number:\n'))
                num2 = float(input('Enter the second number:\n'))
                result = divide(num1, num2)
                print(f'the result of {num1} / {num2} = {result}.')
            except ValueError:
                print('*Enter a number!*')

        elif choice == '5':
            try:
                num1 = float(input('Enter the number:\n'))
                percentage = float(input('Enter the percentage:\n'))
                result = calculate_percentage(num1, percentage)
                print(f'{percentage}% of {num1} = {result}')
            except ValueError:
                print('*Enter a number!*')

        elif choice == '6':
            try:
                num1 = float(input('Enter the number:\n'))
                result = calculate_square_root(num1)
                print(f'The square root of {num1} is {result}')
            except ValueError:
                print('*Enter a number!*')

        elif choice == '7':
            try:
                num1 = float(input('Enter the number:\n'))
                exponent = float(input('Enter the exponent:\n'))
                result = calculate_exponentiation(num1, exponent)
                print(f'{num1} raised to {exponent} = {result}')
            except ValueError:
                print('*Enter a number!*')
