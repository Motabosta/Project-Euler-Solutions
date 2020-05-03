# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers


def initialise_numbers(file_name):
    fileHandler = open(file_name, 'r').readlines()
    fileHandler = [line.strip('\n\r') for line in fileHandler]
    numbers = [int(i) for i in fileHandler]
    return numbers


def find_sum(file_name):
    numbers = initialise_numbers(file_name)
    sum = 0
    for i in numbers:
        sum += i

    answer = str(sum)[:10]
    return int(answer)


print(find_sum('Eular13.txt'))
