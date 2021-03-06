""" You have a number and you need to determine which digit in this number is the biggest.

Input: A positive int.

Output: An Int (0-9). """

def max_digit(number: int) -> int:
  return max([int(digit) for digit in str(number)])


if __name__ == '__main__':
  print("Example:")
  print(max_digit(0))

  assert max_digit(0) == 0
  assert max_digit(52) == 5
  assert max_digit(634) == 6
  assert max_digit(1) == 1
  assert max_digit(10000) == 1
  print("Coding completed!")