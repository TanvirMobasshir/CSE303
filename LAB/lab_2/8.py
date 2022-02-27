nums = [i for i in range(1, 1001)]
divisors = [i for i in range(1, 10)]
highest_divisors = {number: divisor for number in nums for divisor in divisors if number % divisor == 0}
print(highest_divisors)
