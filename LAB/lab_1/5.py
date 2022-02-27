def prime_find_2019_2_60_025(num: int):
    for n in range(2, int(num ** 1 / 2) + 1):
        if num % n == 0:
            return False
    return True


if __name__ == '__main__':
    print("Problem 5")
    print("ID: 2019-2-60-025")
    print()

    n = int(input("Enter a number: "))
    if n <= 0:
        while True:
            n = int(input("Invalid input. Please enter a positive number: "))
            if n > 0: break

    print("The number is prime") if prime_find_2019_2_60_025(n) else print("The number is not prime")
