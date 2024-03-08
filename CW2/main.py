import random


def Z1():
    for i in range(0, 5):
        print(random.randint(1, 100))


def Z2(a, b, c):
    maxNumber = a
    if a < b:
        maxNumber = b
    if b < c:
        maxNumber = c
    print(maxNumber)


def Z3():
    a = int(input('Podaj a: '))
    b = int(input('Podaj b: '))
    c = int(input('Podaj c: '))

    print(a ** 2 + b ** 2 == c ** 2)


def Z4():
    a = float(input('Podaj a: '))
    b = float(input('Podaj b: '))
    c = float(input('Podaj c: '))

    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Nie ma miejsc zerowych")
        return
    elif delta == 0:
        print(((-1) * b - delta) / 2 * a)
        return
    else:
        print(((-1) * b - delta) / 2 * a)
        print(((-1) * b + delta) / 2 * a)


def Z5():
    x = 0
    while x < 10:
        print(3 * x)
        x += 1


def Z6():
    for i in range(1, 11):
        for y in range(1, 11):
            print(i, 'razy', y, '=', i * y)


def Z7():
    wystapienia = 0
    for i in range(1000, 9999):
        x = i // 100
        y = i % 100
        if x ** 2 + y ** 2 == i:
            print(i)
            wystapienia += 1
    print('wystapienia:', wystapienia)


def Z8(k):
    a0 = 1
    a1 = 2
    an = 3


if __name__ == '__main__':
    # Z1()
    # Z2(1, 2, 2)
    # Z3()
    # Z4()
    # Z5()
    # Z6()
    # Z7()
    Z8(8)
