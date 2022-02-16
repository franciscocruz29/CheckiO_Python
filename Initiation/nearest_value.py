""" Find the nearest value to the given one. You are given a list of values as set form and a value for which you need to find the nearest one.

A few clarifications:

  If 2 numbers are at the same distance, you need to choose the smallest one;
  The set of numbers is always non-empty, i.e. the size is >=1;
  The given value can be in this set, which means that it’s the answer;
  The set can contain both positive and negative numbers, but they are always integers;
  The set isn’t sorted and consists of unique numbers.

Input: Two arguments. A list of values in the set form. The sought value is an int.

Output: Int. """

def nearest_value(values: set, one: int) -> int:
  closest_value = min(values, key=lambda x: (abs(x - one), x))
  return closest_value


if __name__ == "__main__":
  print("Example:")
  print(nearest_value({4, 7, 10, 11, 12, 17}, 9))


  assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
  assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
  assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
  assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
  assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
  assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
  assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
  assert nearest_value({5}, 5) == 5
  assert nearest_value({5}, 7) == 5
  assert nearest_value({0, -2}, -1) == -2
  print("Coding completed!")