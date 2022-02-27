def remove_characters(s: str, n: int):
    new_string = ''
    for i in range(n, len(s)):
        new_string = new_string + s[i]

    return new_string


if __name__ == '__main__':
    print("Problem 12")
    print("ID: 2019-2-60-025")
    print()

    s = input("Enter a string: ")
    index = int(input("Enter the index number: "))

    print(f"New string after removing characters: {remove_characters(s, index)}")
