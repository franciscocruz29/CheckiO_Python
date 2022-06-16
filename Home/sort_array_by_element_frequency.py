""" Sort the given Array so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. 
If two elements have the same frequency, they should end up in the same order as the first appearance in the Array.

Input: Iterable

Output: Iterable """


def frequency_sort(items):
    dictionary = {}
    for i in items:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    dictionary = sorted(dictionary.items(), key=lambda k: k[1], reverse=True)
    result = []
    for i in dictionary:
        for j in range(i[1]):
            result.append(i[0])
    return result

    # return sorted(items, key=lambda x: (-items.count(x), items.index(x)))


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [
        4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == [
        'bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([1, 2, 2, 1])) == [1, 1, 2, 2]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete!")
