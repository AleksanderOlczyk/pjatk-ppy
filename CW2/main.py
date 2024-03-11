import random
import math


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


def Z8():
    k = int(input("Podaj wartość k: "))
    a0, a1 = 1, 2

    while True:
        current_term = 3 * a1 + a0

        if current_term > k:
            print(f"Najmniejszy wyraz większy od {k}: {current_term}")
            break

        a0, a1 = a1, current_term


def Z9(x, eps):
    x_rad = math.radians(x)
    x = x_rad % (2 * math.pi)

    if x <= math.pi / 2:
        print(sum(((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1) for i in range(eps)))
    elif x <= math.pi:
        print(sum(((-1) ** i) * ((math.pi - x) ** (2 * i + 1)) / math.factorial(2 * i + 1) for i in range(eps)))
    elif x <= 3 * math.pi / 2:
        print(sum(((-1) ** i) * ((x - math.pi) ** (2 * i + 1)) / math.factorial(2 * i + 1) for i in range(eps)))
    else:
        print(sum(((-1) ** i) * ((2 * math.pi - x) ** (2 * i + 1)) / math.factorial(2 * i + 1) for i in range(eps)))


def Z10():
    limit = 1000000
    catalan_numbers = [1]
    n = 0
    even_count = 0

    while True:
        next_catalan = (4 * n + 2) // (n + 2) * catalan_numbers[-1]

        if next_catalan >= limit:
            break

        catalan_numbers.append(next_catalan)

        if next_catalan % 2 == 0:
            even_count += 1

        n += 1

    odd_count = len(catalan_numbers) - even_count

    print(f"Liczby Catalana mniejsze od {limit}:")
    print(catalan_numbers)
    print(f"\nIlosc liczb parzystych: {even_count}")
    print(f"Ilosc liczb nieparzystych: {odd_count}")


def ZD2():
    k = int(input("Podaj liczbę wartości y: "))

    for x in [i / 10 for i in range(1, 11)]:
        print(f"\nArgument x: {x}")

        for _ in range(k):
            y = float(input("Podaj wartość y: "))
            result = f(x, y)
            print(f"Argument y: {y}, Wartość funkcji: {result}")


def f(x, y):
    if math.sin(x) > math.cos(y):
        result = sum([(x + y)**i / math.factorial(i) for i in range(1, 11)])
    else:
        result = x**5 + x**3 * y**2 + y**4
    return result


if __name__ == '__main__':
    # Z1()
    # Z2(1, 2, 2)
    # Z3()
    # Z4()
    # Z5()
    # Z6()
    # Z7()
    # Z8()
    # Z9(45, 15)
    Z10()
    # ZD2()

