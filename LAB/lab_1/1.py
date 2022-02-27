def my_function(a: int, b: int):
    return a * b if a * b <= 1000 else a + b


if __name__ == '__main__':
    print("Problem 1")
    print("ID: 2019-2-60-025")
    print()

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(my_function(a, b))
