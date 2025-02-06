from utils.date_time import from_unix, get_date, get_time

class Booking:
    def __init__(self, booking_id, user_id, room_id, unix_datetime_start, unix_datetime_end):
        self.booking_id = booking_id
        self.user_id = user_id
        self.room_id = room_id
        self.unix_datetime_start = unix_datetime_start
        self.unix_datetime_end = unix_datetime_end

    def duration(self):
        return self.unix_datetime_end - self.unix_datetime_start

    def is_active(self, current_time):
        return self.unix_datetime_start <= current_time <= self.unix_datetime_end

    def __str__(self):
        start_date = get_date(self.unix_datetime_start)
        start_time = get_time(self.unix_datetime_start)
        end_time = get_time(self.unix_datetime_end)
        return f'Booking details: {self.booking_id} | {self.room_id} | {start_date} {start_time} - {end_time} | {self.user_id}'


    # TODO добавить геттеры и сеттеры
    # TODO добавить @property для валидации значений