import datetime
import math


def Z1():
    print('Hello')
    print('word')


def Z2():
    imie = input("Podaj imie: ")
    rokUrodzenia = int(input("Podaj rok urodzenia: "))
    wiek = datetime.datetime.now().year - rokUrodzenia
    print("Rocznikowo masz", wiek, "lat")


def Z3():
    a = 37
    b = 11
    print(a // b)


def Z4():
    a = 37
    b = 11
    print(a % b)


def Z5():
    a = float(input("Podaj bok a: "))
    b = float(input("Podaj bok b: "))
    print("Pole prostokata jest rowne:", a * b)


def Z6():
    print(round(math.pi, 3))


def Z7():
    a = float(input("Podaj liczbe a: "))
    b = float(input("Podaj liczbe b: "))
    print("suma", a + b)
    print("roznica", a - b)
    print("iloraz", a / b)
    print("iloczyn", a * b)
    print("rownanie", (a + b)**(1/2))
    print("a^b", a**b)
    print("b^a", b**a)


def ZD1():
    print("Podaj wspolrzedne kartezjanskie punktu w przestrzeni")
    x = float(input("x: "))
    y = float(input("y: "))
    z = float(input("z: "))

    print("\nTwoje wspolrzedne w ukladzie sferycznym")
    print("r:", math.sqrt(x**2 + y**2 + z**2))
    print("θ:", math.acos(z/(x**2 + y**2 + z**2)))
    print("ϕ:", math.atan(y / z))

    print("\nTwoje wspolrzedne w ukladzie cylindrycznym")
    print("ρ:", math.sqrt(x**2 + y**2))
    print("ϕ:", math.atan(x / y))
    print("z:", z)


if __name__ == '__main__':
    # Z1()
    # Z2()
    # Z3()
    # Z4()
    # Z5()
    # Z6()
    # Z7()
    ZD1()