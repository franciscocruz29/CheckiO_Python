""" Your task is simple - convert the input date and time from computer format into a "human" format.

Input: Date and time as a string

Output: The same date and time, but in a more readable format """


# NB: words "hour" and "minute" are to be used only when time is 01:mm (1 hour) or hh:01 (1 minute).
# In other cases "hours" and "minutes" should be used.

months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
          7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}


def date_time(time: str) -> str:
    date, time = time.split()
    day, month, year = map(int, date.split('.'))
    hour, minute = map(int, time.split(':'))
    return f'{day} {months[month]} {year} year {hour} hour{"" if hour == 1 else "s"} {minute} minute{"" if minute == 1 else "s"}'


if __name__ == "__main__":
    print("Example:")
    print(date_time("01.01.2000 00:00"))

    assert (
        date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    ), "Millenium"
    assert (
        date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
    ), "Victory"
    assert (
        date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    ), "Somebody was born"

    print("Coding complete!")
