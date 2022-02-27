def series(N:int):
    series_sum = 0
    for i in range(1, N+1):
        series_sum = series_sum + i*i

    return series_sum


if __name__ == '__main__':
    print("Problem 4")
    print("ID: 2019-2-60-025")
    print()

    n = int(input("Enter a number: "))
    if n <= 0:
        while True:
            n = int(input("Invalid input. Please enter a positive number: "))
            if n > 0: break

    print(f"Sum of the Series: {series(n)}")
