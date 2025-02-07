from datetime import datetime


def from_unix(unix_timestamp):
    """
    Converts unix timestamp to datetime tuple.
    Date is presented in DD.MM.YYYY format.
    Time is presented in HH:MM format.

    :param unix_timestamp: unix timestamp number (integer)
    :return: datetime tuple {'date': "%d.%m.%Y", 'time': "%H:%M"}
    """
    dt = datetime.fromtimestamp(unix_timestamp)
    return {'date': dt.strftime("%d.%m.%Y"), 'time': dt.strftime("%H:%M")}


def to_unix(date_str, time_str):
    """
    Converts date and time to unix timestamp.

    :param date_str: Date string presented in DD.MM.YYYY format
    :param time_str: Time string presented in HH:MM format
    :return: unix timestamp (integer)
    """
    dt = datetime.strptime(f"{date_str} {time_str}", "%d.%m.%Y %H:%M")
    return int(dt.timestamp())


def get_date(unix_datetime):
    """
    Returns date from unix timestamp.

    :param unix_datetime: unix timestamp number (integer)
    :return: date string in DD.MM.YYYY format
    """
    return from_unix(unix_datetime)['date']


def get_time(unix_datetime):
    """
    Returns time from unix timestamp.

    :param unix_datetime: unix timestamp number (integer)
    :return: date string in HH:MM format
    """
    return from_unix(unix_datetime)['time']
