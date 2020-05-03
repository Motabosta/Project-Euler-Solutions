# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
palindromes = []
def palindromeChecker(number):
    number = str(number)
    left = 0
    right = len(number)-1

    while left <= right:
        if number[left] != number[right]: return False
        left += 1
        right -= 1
    return True


for a in range(999, 101, -1):
    for b in range(999, 101, -1):
        number = a * b
        if palindromeChecker(number):
            palindromes.append(number)

print(max(palindromes))


