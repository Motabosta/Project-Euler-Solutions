# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.


def collatz_sequence():
    limit = 1000000
    index = currentNum = 0
    chainLength = []

    while index < limit:
        currentNum = index
        counter = 0
        while currentNum > 1:
            if currentNum % 2 == 0:
                currentNum = currentNum / 2
            else:
                currentNum = 3*currentNum + 1
            counter += 1

        chainLength.append(counter)
        index += 1

    maxLength = max(chainLength)
    answer = chainLength.index(maxLength)
    return maxLength, answer

print(collatz_sequence())
