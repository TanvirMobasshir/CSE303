print("Student ID: 2019-2-60-025")
print("Problem 8\n")

nums = [i for i in range(1, 1001)]
highest_divisors = {i: max(j for j in range(2, 10) if i % j == 0) for i in nums if [j for j in range(2, 10) if i % j == 0]}
print(highest_divisors)
