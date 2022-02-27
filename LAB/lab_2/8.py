nums = [i for i in range(1, 1001)]
divisors = [i for i in range(1, 10)]
highest_divisors = {number: divisor for number in nums for divisor in reversed(divisors) if number % divisor == 0}

# highest_divisors = {}
# for i in nums:
#     for j in reversed(divisors):
#         if i % j == 0:
#             highest_divisors[i] = j
print(highest_divisors)
