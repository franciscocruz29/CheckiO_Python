""" You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

Input: A positive integer.

Output: The product of the digits as an integer. 

Precondition: 0 < number < 10^6 """

# Understand the problem:

#  You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.
#  For example: The number given is 123405. The result will be 1*2*3*4*5=120

# Algorithm:
# 1. Convert the number to a string
# 2. Convert the string to a list
# 3. Remove the zeroes from the list
# 4. Multiply the remaining digits
# 5. Convert the list to a string
# 6. Convert the string to an integer
# 7. Return the integer value


def checkio(number: int) -> int:
    res = 1
    for d in str(number):
        if int(d):  # bool(0) is False
            res *= int(d)
    return res

if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))

    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete!")
