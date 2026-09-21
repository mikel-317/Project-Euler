#fidning sum of primes < 2million
#First attempt, skipped eve numbers to make it a tad bit quicker

primes = [2]
for num in range(3, 2000000, 2):
    is_prime = True

    for i in primes:
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)

print(sum(primes))

#Improvement for optimision, so we dont have to test every single case
primes = [2]
for num in range(3, 2000000, 2):
    is_prime = True

    for i in primes:
        if i*i > num:
            break
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)


print(sum(primes))
