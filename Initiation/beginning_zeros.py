""" You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.

Input: A string, that consist of digits.

Output: An Int. """

def beginning_zeros(number: str) -> int:
  count = 0
  for digit in number:
    if digit == '0':
      count += 1
    else:
      break

  return count


if __name__ == '__main__':
  print("Example:")
  print(beginning_zeros('100'))

  assert beginning_zeros('100') == 0
  assert beginning_zeros('001') == 2
  assert beginning_zeros('100100') == 0
  assert beginning_zeros('001001') == 2
  assert beginning_zeros('012345679') == 1
  assert beginning_zeros('0000') == 4
  print("Coding completed!")