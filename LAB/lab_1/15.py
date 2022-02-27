def problem_15(list1: list, list2: list):
    new_list = []
    for i in list1:
        if i % 2 != 0:
            new_list.append(i)

    for j in list2:
        if j % 2 == 0:
            new_list.append(j)

    return new_list


if __name__ == '__main__':
    print("Problem 15")
    print("ID: 2019-2-60-025")
    print()

    l1 = [5, 54, 8, 6, 59, 10]
    l2 = [10, 5, 69, 55, 6, 5]

    print(f"New List: {problem_15(l1, l2)}")
