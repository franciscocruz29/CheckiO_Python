""" In this mission you need to create a password verification function.

Those are the verification conditions:

  the length should be bigger than 6
  should contain at least one digit.

Input: A string.
Output: A bool. """


def is_acceptable_password(password: str) -> bool:
    # C1 : the length should be bigger than 6;
    # C2 : should contain at least one digit.
    c1 = len(password) > 6
    c2 = any(map(str.isdigit, password))
    return c1 and c2


if __name__ == "__main__":
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == False
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    print("Coding complete!")
