nums = [i for i in range(1, 1001)]
numbers = list(set([i for i in nums for j in range(2, 10) if i % j == 0]))
print(numbers)
