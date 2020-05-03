# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

testingNum = 600851475143
primeFactors = []
factor = 1

while testingNum != 1:
    testingNum = (testingNum/factor) if testingNum % factor == 0 else testingNum
    primeFactors.append(factor)
    factor += 1

print(max(primeFactors))
