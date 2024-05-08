import datetime
from unittest.mock import Mock

year1 = datetime.datetime(2020, 1, 1)
year2 = datetime.datetime(2021, 1, 1)

datetime = Mock()

def is_leap_year():
    today = datetime.datetime.today()
    return today.year % 400 == 0 or (today.year % 4 == 0 and today.year % 100 != 0)

def test_is_leap_year():
    # Testati in minim 2 moduri functia is_leap_year, folosind mock.
    datetime.datetime.today.return_value = year1
    assert is_leap_year()

    datetime.datetime.today.return_value = year2
    assert not is_leap_year()
