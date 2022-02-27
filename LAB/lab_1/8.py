def even_indexed_sum(l: list):
    s = 0
    for i in range(len(l)):
        if i % 2 == 0:
            s = s + l[i]

    return s


if __name__ == '__main__':
    print("Problem 8")
    print("ID: 2019-2-60-025")
    print()

    l = [5, 54, 8, 6, 59, 10]

    print(f"Sum of even indexed elements: {even_indexed_sum(l)}")
