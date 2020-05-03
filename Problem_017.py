# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.


def decide_wording(number):
    counter = 0
    # numPos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
    wordings = [0, 3, 3, 5, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 9, 8, 8, 6, 6, 5, 5, 5, 7, 6, 6, 7, 8]
    # pos    = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90,100,1000]

    tens = int(str(number)[-2:])

    # Remember to add the and
    if number >= 1000:
        thousands = int(str(number)[-4:-3])
        counter = counter + number[thousands] + number[27]
    if number >= 100:
        hundreds = int(str(number)[-3:-2])
        counter = counter + number[hundreds] + number[27]
    if number > 20:
        tens = int(str(number)[-2:-1])
        ones = int(str(number)[-1])
        counter = 0  # wtf


    return counter


def number_letter_counts(limit):
    totalCount = 0
    index = 0
    totalCount += decide_wording(index)

    #for i in range(limit+1):
        #totalCount += decide_wording(i)

    return totalCount


print(number_letter_counts(1000))
