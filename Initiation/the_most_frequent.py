""" You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence. It can be only one.

Input: non empty list of strings.

Output: a string. """

def most_frequent(data: list) -> str:
  return max(data, key=data.count)


if __name__ == "__main__":
  
  print("Example:")
  print(most_frequent(["a", "b", "c", "a", "b", "a"]))

  assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
  assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

  print("Done")