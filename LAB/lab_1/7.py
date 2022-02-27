def sum_of_list(l: list):
    s = 0
    for i in l:
        s = s+i

    return s


if __name__ == '__main__':
    print("Problem 7")
    print("ID: 2019-2-60-025")
    print()

    l = [5, 54, 8, 6, 59, 10]

    print(f"Sum of the list: {sum_of_list(l)}")
