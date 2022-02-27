def largest_number_2019_2_60_025(l: list):
    max_num = l[0]
    for i in l:
        if max_num < i:
            max_num = i

    return max_num


def smallest_number_2019_2_60_025(l: list):
    min_num = l[0]
    for i in l:
        if min_num > i:
            min_num = i

    return min_num


if __name__ == '__main__':
    print("Problem 9")
    print("ID: 2019-2-60-025")
    print()

    l = [5, 54, 8, 6, 59, 10]

    print(f"Largest Number: {largest_number_2019_2_60_025(l)}")
    print(f"Smallest Number; {smallest_number_2019_2_60_025(l)}")
