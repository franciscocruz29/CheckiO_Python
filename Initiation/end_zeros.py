""" Try to find out how many zeros a given number has at the end.

Input: A positive Int

Output: An Int. """

def end_zeros(num: int) -> int:
  count = 0
  strNum = str(num)[::-1]
  for number in strNum:
    if number == '0':
      count += 1
    else:
      break
  return count


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding completed!")