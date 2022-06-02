""" In a given text you need to sum the numbers while excluding any digits that form part of a word.

The text consists of numbers, spaces and letters from the English alphabet.

Input: A string.

Output: An int. """

""" def sum_numbers(text: str) -> int:
    words = text.split()
    count = 0
    for word in words:
        try:
            count += int(word)
        except ValueError:
            pass
    return count """

sum_numbers = lambda text: sum(int(word) for word in text.split() if word.isdigit())

# isdigit(), Check if all the characters in the text are digits

if __name__ == "__main__":
    print("Example:")
    print(sum_numbers("hi"))

    
    assert sum_numbers("hi") == 0
    assert sum_numbers("who is 1st here") == 0
    assert sum_numbers("my numbers is 2") == 2
    assert (
        sum_numbers(
            "This picture is an oil on canvas "
            "painting by Danish artist Anna "
            "Petersen between 1845 and 1910 year"
        )
        == 3755
    )
    assert sum_numbers("5 plus 6 is") == 11
    assert sum_numbers("") == 0
    print("Coding complete!")