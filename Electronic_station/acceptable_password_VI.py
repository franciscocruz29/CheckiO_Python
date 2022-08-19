""" In this mission you need to create a password verification function.

Those are the verification conditions:

  the length should be bigger than 6
  should contain at least one digit, but it cannot consist of just digits
  having numbers or containing just numbers does not apply to the password longer than 9.
  a string should not contain the word "password" in any case
  should contain at least 3 different letters ( or digits) even if it is longer than 10

Input: A string.
Output: A bool. """


def is_acceptable_password(password: str) -> bool:
    # C1 : the length should be bigger than 6;
    # C2 : should contain at least one digit, but cannot consist of just digits.
    # C3 : having numbers or containing just numbers does not apply to the password longer than 9.
    # C4 : a string should not contain the word "password" in any case.
    # C5 : should contain at least 3 different letters ( or digits) even if it is longer than 10
    c1 = len(password) > 6
    c2 = any(map(str.isdigit, password)) and not password.isdigit()
    c3 = len(password) > 9
    c4 = "password" not in password.lower()
    c5 = len(set(password)) >= 3
    return c1 and (c2 or c3) and c4 and c5


if __name__ == "__main__":
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True
    assert is_acceptable_password("password12345") == False
    assert is_acceptable_password("PASSWORD12345") == False
    assert is_acceptable_password("pass1234word") == True
    assert is_acceptable_password("aaaaaa1") == False
    assert is_acceptable_password("aaaaaabbbbb") == False
    assert is_acceptable_password("aaaaaabb1") == True
    assert is_acceptable_password("abc1") == False
    assert is_acceptable_password("abbcc12") == True
    print("Coding complete!")
