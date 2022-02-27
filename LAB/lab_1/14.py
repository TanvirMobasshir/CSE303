def palindrome_checker_2019_2_60_025(s: str):
    return s == s[::-1]


if __name__ == '__main__':
    print("Problem 14")
    print("ID: 2019-2-60-025")
    print()

    s = input("Enter a string: ")
    print(f"The string is {'a palindrome' if palindrome_checker_2019_2_60_025(s) else 'not a palindrome'}")
