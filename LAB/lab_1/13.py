def count_substring(main_str, sub_str):
    count = 0
    for i in range(len(main_str) - len(sub_str) + 1):
        if main_str[i: i + len(sub_str)] == sub_str:
            count += 1

    return count


if __name__ == '__main__':
    print("Problem 13")
    print("ID: 2019-2-60-025")
    print()

    main_string = input("Enter a string: ")
    print(f"Number of CSE303 occurrences in the given string is {count_substring(main_string, 'CSE303')}")
