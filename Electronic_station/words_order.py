""" You have a text and a list of words. You need to check if the words in a list appear in the same order as in the given text.

Cases you should expect while solving this challenge:

  a word from the list is not in the text - your function should return False
  any word can appear more than once in a text - use only the first one
  two words in the given list are the same - your function should return False
  the condition is case sensitive, which means 'hi' and 'Hi' are two different words
  the text includes only English letters and spaces.

Input: Two arguments. The first one is a given text, the second is a list of words.

Output: A bool. """

""" Algorithm:
    1. Check if the words list are unique if not return False
    1. Split the text into words
    2. Check if the words in the list are in the text
    3. Return True if the words in the list are in the text and False otherwise
"""


def words_order(text: str, words: list) -> bool:
    if len(words) != len(set(words)):
        return False

    return [word for word in text.split() if word in words] == words


if __name__ == "__main__":
    print("Example:")
    print(words_order("hi world im here", ["world", "here"]))

    assert words_order("hi world im here", ["world", "here"]) == True
    assert words_order("hi world im here", ["here", "world"]) == False
    assert words_order("hi world im here", ["world"]) == True
    assert words_order("hi world im here", ["world", "here", "hi"]) == False
    assert words_order("hi world im here", ["world", "im", "here"]) == True
    assert words_order("hi world im here", ["world", "hi", "here"]) == False
    assert words_order("hi world im here", ["world", "world"]) == False
    assert words_order("hi world im here", ["country", "world"]) == False
    assert words_order("hi world im here", ["wo", "rld"]) == False
    assert words_order("", ["world", "here"]) == False
    assert words_order("hi world world im here", ["world", "world"]) == False
    print("Coding complete!")
