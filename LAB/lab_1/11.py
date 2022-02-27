def second_index_characters(s: str):
    for i in range(len(s)):
        if i % 2 == 0: print(s[i])


if __name__ == '__main__':
    print("Problem 11")
    print("ID: 2019-2-60-025")
    print()

    s = input("Enter a string: ")
    second_index_characters(s)
