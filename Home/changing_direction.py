""" Given a list of integers. Your task in this mission is to find how many times sorting directions was changed in the given list.

Input: List.

Output: Int.

Examples:

changing_direction([1, 2, 3, 4, 5]) == 0
changing_direction([1, 2, 3, 2, 1]) == 1
changing_direction([1, 2, 2, 1, 2, 2]) == 2

Precondition:
* the list is non-empty
* the elements in the list are positive integers
"""

""" 

Understanding the problem:

Given a list of integers, find a way to count elements wwhich are either peak (x > y < z) or valley (x < y > z)

Algorithm:

1. Get rid of adjacent equal values.
2. Iterate for each element and check if its next and previous element is either smaller or larger than the current element. 
3. If found, the counter is incremented.

"""




from itertools import groupby
def changing_direction(elements: list) -> int:
    res = 0
    elements = [n for n, g in groupby(elements)]
    for idx in range(1, len(elements) - 1):
        if elements[idx + 1] > elements[idx] < elements[idx - 1] or elements[idx + 1] < elements[idx] > elements[idx - 1]:
            res += 1
    return res


assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2
assert changing_direction([0]) == 0
assert changing_direction([1, 2, 3, 5, 4, 2, 5, 7, 8, 3, 2, 1]) == 3
assert changing_direction([6, 6, 6, 4, 1, 2, 5, 9, 7, 8, 5, 9, 4, 2, 6]) == 7
assert changing_direction([2, 2, 2, 2, 2, 1]) == 0

print("The mission is done!")
