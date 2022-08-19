""" In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6
should contain at least one digit, but cannot consist of just digits.

Input: A string.
Output: A bool. """


def is_acceptable_password(password: str) -> bool:
    # C1 : the length should be bigger than 6;
    # C2 : should contain at least one digit.
    # C3 : cannot consist of just digits.
    c1 = len(password) > 6
    c2 = any(map(str.isdigit, password))
    c3 = not password.isdigit()
    return c1 and c2 and c3


if __name__ == "__main__":
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == False
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    print("Coding complete!")
