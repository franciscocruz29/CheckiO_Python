""" You are given a string with words and numbers separated by whitespaces(one space). 
The words contains only letters. You should check if the string contains three words in succession. 
For example, the string "start 5 one two three 7 end" contains three words in succession.

Input: A string with words.

Output: The answer as a boolean. """


def checkio(words: str) -> bool:
    words = words.split()
    count = 0
    for word in words:
        if word.isalpha():
            count += 1
        else:
            count = 0
        if count == 3:
            return True
    return False


if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    assert checkio("start 5 one two three 7 end") == True, "one two three"
    print("Coding complete!")
