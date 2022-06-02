""" You are given an array of integers. You should find the sum of the integers with even indexes(0th, 2nd, 4th...). 
Then multiply this summed number and the final element of the array together. 

For an empty array, the result will always be 0 (zero).

Input: A list of integers.

Output: The number as an integer. """

""" def checkio(array: list) -> int:
    if len(array) == 0:
        return 0
    else:
        even_sum = 0
        for i in range(0, len(array), 2):
            even_sum += array[i]
        return even_sum * array[-1] """


def checkio(array):
    if len(array) == 0:
        return 0
    return sum(array[0::2]) * array[-1]
    
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))
    
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete!")