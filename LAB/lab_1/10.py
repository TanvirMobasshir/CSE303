def second_largest(l: list):
    l.sort()
    return l[-2]


if __name__ == '__main__':
    print("Problem 10")
    print("ID: 2019-2-60-025")
    print()

    l = [5, 54, 8, 6, 59, 10]

    print(f"Largest Number: {second_largest(l)}")
