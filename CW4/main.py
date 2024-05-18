class Car:
    def __init__(self, brand, year, price):
        self.brand = brand
        self.year = year
        self.price = price


def increase_prices(matrix):
    oldest_car_price = float('inf')
    for i in range(len(matrix[0])):
        youngest_car_price = float('inf')
        for j in range(len(matrix)):
            if j != 0 and j != len(matrix) - 1 and i != len(matrix) - 1:
                youngest_car_price = min(youngest_car_price, matrix[j][i].price)
        for j in range(len(matrix)):
            if j != len(matrix) - 1:
                if matrix[j][i].price < matrix[len(matrix) - 1][i].price:
                    matrix[j][i].price += youngest_car_price
        oldest_car_price = min(oldest_car_price, matrix[0][i].price)


def print_cars(matrix):
    oldest_car_price = float('-inf')
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i < j and i + j < len(matrix) - 1:
                oldest_car_price = max(oldest_car_price, matrix[i][j].price)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if 'i' not in matrix[i][j].brand.lower() and 'z' not in matrix[i][j].brand.lower() and matrix[i][
                j].price < oldest_car_price:
                print(f"Brand: {matrix[i][j].brand}, Year: {matrix[i][j].year}, Price: {matrix[i][j].price}")


def increase_cheapest_prices(matrix):
    prices = []
    for i in range(len(matrix)):
        prices.extend([car.price for car in matrix[i]])
    prices.sort()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (i == j or i + j == len(matrix) - 1) and matrix[i][j].price in prices[:2]:
                matrix[i][j].price += 15


def create_car_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            # brand = input(f"Enter brand of car at position [{i}][{j}]: ")             # losowe dane dla testów
            # year = int(input(f"Enter year of car at position [{i}][{j}]: "))          # losowe dane dla testów
            # price = float(input(f"Enter price of car at position [{i}][{j}]: "))      # losowe dane dla testów
            brand = input(f"Enter brand of car at position [{i}][{j}]: ")
            year = int(input(f"Enter year of car at position [{i}][{j}]: "))
            price = float(input(f"Enter price of car at position [{i}][{j}]: "))
            print("\n\n")
            row.append(Car(brand, year, price))
        matrix.append(row)
    return matrix


def main():
    n = int(input("Enter the size of the square matrices: "))

    print("\nCreating first matrix:")
    matrix1 = create_car_matrix(n)
    increase_prices(matrix1)
    print("\nCars after increasing prices:")
    print_cars(matrix1)
    increase_cheapest_prices(matrix1)
    print("\nCars after increasing prices of cheapest on diagonals:")
    print_cars(matrix1)

    print("\nCreating second matrix:")
    matrix2 = create_car_matrix(n)
    increase_prices(matrix2)
    print("\nCars after increasing prices:")
    print_cars(matrix2)
    increase_cheapest_prices(matrix2)
    print("\nCars after increasing prices of cheapest on diagonals:")
    print_cars(matrix2)


if __name__ == "__main__":
    main()
