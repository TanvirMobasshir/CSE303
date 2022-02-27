def fib(n: int):
    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 1

    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print("Problem 6")
    print("ID: 2019-2-60-025")
    print()

    n = int(input("Enter a number: "))
    if n < 0:
        while True:
            n = int(input("Invalid input. Please enter a positive number: "))
            if n >= 0: break

    print(f"Fibonacci Number: {fib(n)}")
