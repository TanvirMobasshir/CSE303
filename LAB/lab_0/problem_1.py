def valid(a, b, c):
    if a > b + c: return False
    if b > a + c: return False
    if c > a + b: return False
    return True


def area(a, b, c):
    s = (a + b + c) / 2
    x = s * (s - a) * (s - b) * (s - c)
    return pow(x, 0.5)


if __name__ == "__main__":

    print("Student ID: 2019-2-60-025\n")

    a = int(input('First side: '))
    b = int(input('Second side: '))
    c = int(input('Third side: '))
    print()
    print('Area: ' + str("{:.2f}".format(area(a, b, c)))) if valid(
        a, b, c) else print("Invalid Triangle")
