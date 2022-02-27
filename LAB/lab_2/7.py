nums = [i for i in range(1, 1001)]
numbers = []

for i in nums:
    for j in range(2, 10):
        if i % j == 0:
            numbers.append(i)
            break

print(numbers)
