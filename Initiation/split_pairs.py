""" Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').

Input: A string.

Output: An iterable of strings. """

def split_pairs(s):
  N = len(s)
  if N % 2 == 1: 
    s += "_"
  return [s[i:i+2] for i in range(0, N, 2)]


if __name__ == '__main__':
  print("Example:")
  print(list(split_pairs('abcd')))
  
  assert list(split_pairs('abcd')) == ['ab', 'cd']
  assert list(split_pairs('abc')) == ['ab', 'c_']
  assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
  assert list(split_pairs('a')) == ['a_']
  assert list(split_pairs('')) == []
  print("Coding completed!")