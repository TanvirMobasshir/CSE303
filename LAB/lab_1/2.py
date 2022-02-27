def area(r: float):
    return 3.14415 * r * r


def perimeter(r: float):
    return 2 * 3.1416 * r


if __name__ == '__main__':
    print("Problem 2")
    print("ID: 2019-2-60-025")
    print()

    r = float(input("Enter radius of the circle: "))
    print(f"Area: {area(r)}")
    print(f"Perimeter: {perimeter(r)}")
