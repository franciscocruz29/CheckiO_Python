""" You are given two strings and you have to find an index of the second occurrence of the second string in the first one.

Input: Two strings.

Output: Int or None """


def second_index(text: str, symbol: str) -> [int, None]:
  try:
    return text.index(symbol, text.index(symbol) + 1)
  except ValueError:
    return None
 

if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('All tests are done!')
