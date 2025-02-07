class Booking:
    def __init__(self, booking_id, user_id, room_id, unix_datetime_start, unix_datetime_end):
        self.booking_id = booking_id
        self.user_id = user_id
        self.room_id = room_id
        self.unix_datetime_start = unix_datetime_start
        self.unix_datetime_end = unix_datetime_end
