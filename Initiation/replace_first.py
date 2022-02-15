from typing import Iterable

""" In a given list the first element should become the last one. An empty list or list with only one element should stay the same.

example

Input: List.

Output: Iterable. """

def replace_first(items: list) -> Iterable:
  return [] if len(items) == 0 else items[1:] + [items[0]]


if __name__ == "__main__":
  print("Example:")
  print(list(replace_first([1, 2, 3, 4])))

  assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
  assert list(replace_first([1])) == [1]
  assert list(replace_first([])) == []
  print("Coding completed!")