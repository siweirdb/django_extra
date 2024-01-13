import math


def insert():
    while True:
        number1 = input("insert a: ")
        number2 = input("insert b: ")
        if not number1.isnumeric() or not number2.isnumeric():
            print(
                "You have entered a string, enter a number to continue using the calculator"
            )
        else:
            number1 = int(number1)
            number2 = int(number2)
            break

    return number1, number2


def plus(a: int, b: int):
    print(f"Answer a+b: {a + b}")


def minus(a: int, b: int):
    print(f"Answer a-b: {a - b}")


def multiply(a: int, b: int):
    print(f"Answer a * b: {a * b}")


def divide(a: int, b: int):
    print(f"Answer a / b: {a / b}")


def square_root(x: int):
    print(f"Answer √x: {math.sqrt(x)}")


def mod(a: int, b: int):
    print(f"Answer a % b: {a % b}")


def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    first, second = int(0), int(1)
    while n != 1:
        temp = second
        second = first + second
        first = temp
        n -= 1
    return second


while True:
    print("1. a + b")
    print("2. a - b")
    print("3. a * b")
    print("4. a / b")
    print("5. a % b")
    print("6. √x")
    print("7. Fibonacci number")
    print("8. Exit")

    number = input("Enter option: ")

    if not number.isnumeric():
        print(
            "You have entered a string, enter a number to continue using the calculator"
        )
    else:
        number = int(number)

    if number == 1:
        num1, num2 = insert()
        plus(num1, num2)
    elif number == 2:
        num1, num2 = insert()
        minus(num1, num2)
    elif number == 3:
        num1, num2 = insert()
        multiply(num1, num2)
    elif number == 4:
        num1, num2 = insert()
        divide(num1, num2)
    elif number == 5:
        num1, num2 = insert()
        mod(num1, num2)
    elif number == 6 or number == 7:
        while True:
            a = input("insert number: ")
            if not a.isnumeric():
                print(
                    "You have entered a string, enter a number to continue using the calculator"
                )
            else:
                a = int(a)
                break
        if number == 6:
            square_root(a)
        else:
            print(f"Answer {a}th fibonacci number: {fib(a)}")
    elif number == 8:
        break
    print()
