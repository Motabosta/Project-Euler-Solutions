# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10,001st prime number?

counter = 3
primeNumbers = [2]

while len(primeNumbers) <= 10001:
    for i in range(len(primeNumbers)):
        if counter % primeNumbers[i] == 0:
            break
        elif counter % primeNumbers[i] != 0 and i == len(primeNumbers)-1:
            primeNumbers.append(counter)
    counter += 1

print(primeNumbers[10000])
