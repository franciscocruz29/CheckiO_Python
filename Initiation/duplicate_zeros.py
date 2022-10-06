""" You are given a list of integers. Your task in this mission is to double all the zeros in the given list.

Input: List.

Output: List. """

def my_gen(arr: list):
    for num in arr:
        if num == 0:
            yield 0
            yield 0
        else:
            yield num

def duplicate_zeros(donuts: list) -> list:
    return list(my_gen(donuts))


assert duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]) == [
    1, 0, 0, 2, 3, 0, 0, 4, 5, 0, 0]
assert duplicate_zeros([0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0]
assert duplicate_zeros([100, 10, 0, 101, 1000]) == [100, 10, 0, 0, 101, 1000]
assert duplicate_zeros([1, 0, 0, 1, 0, 0, 1, 1, 0]) == [
    1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0]

print("The mission is done!")
