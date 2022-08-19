""" Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return False.

Input: A string.

Output: a boolean. """


def is_all_upper(text: str) -> bool:
    return text.isupper()


if __name__ == "__main__":
    print("Example:")
    print(is_all_upper("ALL UPPER"))

    assert is_all_upper("ALL UPPER") == True
    assert is_all_upper("all lower") == False
    assert is_all_upper("mixed UPPER and lower") == False
    assert is_all_upper("") == False
    print("Coding complete!")
