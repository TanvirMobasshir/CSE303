print("Student ID: 2019-2-60-025")
print("Problem 7\n")

nums = [i for i in range(1, 1001)]
numbers = [i for i in nums if [j for j in range(2, 10) if i % j == 0]]
print(numbers)
