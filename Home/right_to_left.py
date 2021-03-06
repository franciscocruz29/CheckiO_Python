""" You are given a sequence of strings. You should join these strings into a chunk of text where the initial strings are separated by commas. 
As a joke on the right handed robots, you should replace all cases of the words "right" with the word "left", even if it's a part of another word. 
All strings are given in lowercase.

Input: A sequence of strings.

Output: The text as a comma-separated string. """


def left_join(phrases: tuple) -> str:
    return ','.join(phrases).replace('right', 'left')


if __name__ == "__main__":
    print("Example:")
    print(left_join(("left", "right", "left", "stop")))

    assert (
        left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
    ), "All to left"
    assert left_join(("bright aright", "ok")
                     ) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")
                     ) == "enough,jokes", "Nothing to replace"
    print("Coding complete!")
