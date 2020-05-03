# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def even_divisibility_checker():
    answer = 1
    while True:
        for i in range(1, 21):
            if answer % i != 0:
                break
            elif i == 20:
                return answer
        answer += 1


print(even_divisibility_checker())
