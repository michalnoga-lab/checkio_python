import datetime
from typing import Union


def sun_angle(time: str) -> Union[int, str]:
    time_to_check: datetime = datetime.datetime.strptime(time, '%H:%M')
    start_time: datetime = datetime.datetime.strptime('6:00', '%H:%M')
    end_time: datetime = datetime.datetime.strptime('18:00', '%H:%M')
    difference: datetime = time_to_check - start_time
    return (180 / 720) * difference.seconds / 60 if end_time >= time_to_check >= start_time else 'I don\'t see the sun!'


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
