def compound_interest_2019_2_60_025(P: float, R: float, T: float):
    return P * (1 + pow(R / 100, T))


if __name__ == '__main__':
    print("Problem 3")
    print("ID: 2019-2-60-025")
    print()

    P = float(input("Principle Amount: "))
    R = float(input("Interest Rate: "))
    T = float(input("Time: "))

    print(f"Compound Interest: {compound_interest_2019_2_60_025(P, R, T)}")
