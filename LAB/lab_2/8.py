nums = [i for i in range(1, 1001)]
divisors = [i for i in range(1, 10)]
highest_divisor = {}

for i in nums:
    for j in reversed(divisors):
        if i % j == 0:
            highest_divisor[i] = j
            break

print(highest_divisor)
