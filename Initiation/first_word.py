""" You are given a string and you have to find its first word.

The input string consists of only English letters and spaces.
There aren’t any spaces at the beginning and the end of the string.

Input: A string.

Output: A string. """

def first_word(text: str) -> str:
    """
    returns the first word in a given text.
    """
    return text.split(' ')[0]


if __name__ == "__main__":
      
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding completed!")