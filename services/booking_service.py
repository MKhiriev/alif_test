class BookingService:
    def __init__(self, booking_repository, user_notification_service):
        self.booking_repository = booking_repository
        self.user_notification_service = user_notification_service

    def book_room(self, user_id, room_id, booking_time):
        """
        Books a room.

        :param user_id: id of user who is going to book
        :param room_id: id of room which is going to be booked
        :param booking_time: list with two elements [datetime_start, datetime_end]
        :return: None
        """
        # Check if room available. Use room number and booking time (start, end).
        [available, overlapping_bookings] = self.check_if_available(room_id, booking_time)
        # if room is available then add booking and notify person by email and phone number
        if available:
            new_booking = self.booking_repository.add_room_booking(user_id, room_id, booking_time)
            self.user_notification_service.notify_user(user_id, new_booking)
        # else if room is not available - show booking failed message. Show existing bookings: who booked + booking time
        else:
            print('Room is already booked. Choose another time.')
            for booking in overlapping_bookings:
                print(booking)

    def check_if_available(self, room_id, booking_time):
        """
        Checks room availability by booking time.
        If available, returns True and empty list of overlapping bookings (which means it is available).
        If not available, returns False and list of overlapping bookings.

        :param room_id: id of room which is going to be booked
        :param booking_time: list with two elements [datetime_start, datetime_end]
        :return: If available, returns True and empty list of overlapping bookings (which means it is available).
                 If not available, returns False and list of overlapping bookings.
        """
        room_is_available = True
        room_is_not_available = False

        no_overlapping_bookings = []
        overlapping_bookings = self.booking_repository.get_bookings_by_room_id_and_booking_time(room_id, booking_time)

        if not overlapping_bookings:
            return [room_is_available, no_overlapping_bookings]
        else:
            return [room_is_not_available, overlapping_bookings]
