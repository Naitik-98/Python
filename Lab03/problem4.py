sum_primes = 0

for num in range(2, 1000):
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        sum_primes += num

print("Sum of primes below 1000 =", sum_primes)