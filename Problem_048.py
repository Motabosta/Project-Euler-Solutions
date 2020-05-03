# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.


def self_powers(n):
    sum = 0
    for i in range(1, n):
        sum += i**i
    answer = str(sum)[-10:]
    return answer

print(self_powers(1000))