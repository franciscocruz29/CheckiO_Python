""" You are given a list of integers, which are elements of arithmetic progression - 
the difference between the consecutive elements is constant. But this list is unsorted and one element is missing...good luck!

Input: List of integers.

Output: Integer. 

Preconditions:

length of sequence > 2;
missing element is always between two elements in sequence."""

""" Understand the problem

1. A sequence [arr0, arr1,…, arr(n-1)] is called an Arithmetic progression if for each 'i' ( 0 ≤ i < n - 1) the value arr[i+1] - arr[i] is the same. 
2. There is exactly one missing number in the given sequence.
3. All the numbers present in the sequence are distinct.
4. It is the guarantee that the first and last elements of the sequence are not missing elements.

The common difference d of the Arithmetic Progression having exactly one missing element can be calculated as d = arr[n-1] - arr[0] / n

 """


def missing_number(items: list[int]) -> int:
    sorted_items = sorted(items)
    d = (sorted_items[len(items)-1] - sorted_items[0]) / len(items)
    for i in range(len(items)):
        # if the difference between the current and the next element is not equal to d, then return the answer as current element + d.
        if (sorted_items[i + 1] - sorted_items[i] != d):
            return sorted_items[i] + d


assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4
assert missing_number([5, 25, 30, 20, 15]) == 10
assert missing_number([0, 1, 3, 4, 2, 6, 9, 7, 8]) == 5

print("The mission is done!")
