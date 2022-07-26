from typing import Union

""" Your task is to find the angle of the sun above the horizon knowing the time of the day. 
Input data: the sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees. 
At 12:00 PM the sun reaches its zenith, which means that the angle equals 90 degrees. 
6:00 PM is the time of the sunset so the angle is 180 degrees. 
If the input will be the time of the night(before 6:00 AM or after 6:00 PM), your function should return - "I don't see the sun!".

Input: The time of the day.

Output: The angle of the sun, rounded to 2 decimal places. """

def sun_angle(time: str) -> Union[int, str]:
    time = time.split(':')
    hour = int(time[0])
    minute = int(time[1])
    angle = (hour - 6) * 15 + minute * 0.25
    if angle < 0 or angle > 180:
        return "I don't see the sun!"
    else:
        return round(angle, 2)


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    assert sun_angle("07:00") == 15
    assert sun_angle("12:00") == 90
    assert sun_angle("12:15") == 93.75
    assert sun_angle("18:01") == "I don't see the sun!"
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete!")
