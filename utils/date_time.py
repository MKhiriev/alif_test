from datetime import datetime

def to_unix(date_str, time_str):
    dt = datetime.strptime(f"{date_str} {time_str}", "%d.%m.%Y %H:%M")
    return int(dt.timestamp())


def from_unix(unix_timestamp):
    dt = datetime.fromtimestamp(unix_timestamp)
    return {'date': dt.strftime("%d.%m.%Y"), 'time': dt.strftime("%H:%M")}

def get_date(unix_datetime):
    return from_unix(unix_datetime)['date']

def get_time(unix_datetime):
    return from_unix(unix_datetime)['time']