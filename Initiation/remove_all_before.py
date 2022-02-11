""" What you need to do here is to remove from the list all of the elements before the given one.

We have two edge cases here: 
(1) if a cutting element cannot be found, then the list shoudn't be changed. 
(2) if the list is empty, then it should remain empty.

Input: List and the border element.

Output: Iterable (tuple, list, iterator ...). """

from typing import Iterable

def remove_all_before(items: list, border: int) -> Iterable:
  if border not in items:
    return items
  else:
    return items[items.index(border):]


if __name__ == '__main__':
  print("Example:")
  print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

  assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
  assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
  assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
  assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
  assert list(remove_all_before([], 0)) == []
  assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
  print("Coding completed!")