import random as rand


def Z1():
    liczby = []
    sum = 0
    for i in range (0, 20):
        randomNumber = rand.randint(-10, 20)
        liczby.append(randomNumber)
        sum += randomNumber
    swapPositions(liczby, liczby.index(max(liczby)), liczby.index(min(liczby)))


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def Z3():
    tup = ()
    N = 10
    x = 0

    for i in range(N):
        row = ()
        for j in range(N):
            row += (x, )
            x += 1
        tup += (row, )

    sum = 0
    for i in range(N):
        sum += tup[i][i]
    print(sum)


if __name__ == '__main__':
    # Z1()
    # Z2()
    Z3()
    # Z4()
    # Z5()
    # Z6()
    # Z7()
    # Z8()
    # Z9()
    # Z10()
    # ZD3()
