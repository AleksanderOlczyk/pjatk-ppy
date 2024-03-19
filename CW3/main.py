import random as rand
import numpy as np


def Z1():
    liczby = []
    sum = 0
    for i in range(0, 20):
        randomNumber = rand.randint(-10, 20)
        liczby.append(randomNumber)
        sum += randomNumber
    swapPositions(liczby, liczby.index(max(liczby)), liczby.index(min(liczby)))


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def znajdzTrojkiPitagorejskie(N):
    trojki = []
    for a in range(1, N + 1):
        for b in range(a, N + 1):
            for c in range(b, N + 1):
                if a ** 2 + b ** 2 == c ** 2:
                    trojki.append((a, b, c))
    return trojki


def Z2():
    N = 30
    trojki = znajdzTrojkiPitagorejskie(N)
    for trojka in trojki:
        print(trojka)


def Z3():
    tup = ()
    N = 10
    x = 0

    for i in range(N):
        row = ()
        for j in range(N):
            row += (x,)
            x += 1
        tup += (row,)

    sum = 0
    for i in range(N):
        sum += tup[i][i]
    print(sum)


def ZD3(n, value, K):
    def generate_random_number(X):
        return np.random.uniform(0, X)

    def generate_constrained(i, j):
        return np.random.uniform(-3 * i - 1, 5 * j + 4)

    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i < j:
                A[i][j] = generate_constrained(i, j)
            else:
                A[i][j] = generate_random_number(7)

    print("Array A before shifting:")
    print(A)

    column_sums = np.sum(A, axis=0)

    for i in range(n):
        if column_sums[i] > value:
            A[:, i] = np.roll(A[:, i], -2)  # shift column up by 2 positions
        else:
            A[:, i] = np.roll(A[:, i], K)  # shift column down by K positions

    print("\nArray A after shifting:")
    print(A)


if __name__ == '__main__':
    # Z1()
    # Z2()
    # Z3()
    # Z4()
    # Z5()
    # Z6()
    # Z7()
    # Z8()
    # Z9()
    # Z10()
    value = float(input("Enter a number: "))
    ZD3(5, value, 3)
