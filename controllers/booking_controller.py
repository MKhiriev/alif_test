from utils.datetime_utils import get_date, get_time, to_unix


class BookingController:
    def __init__(self, booking_service, view):
        self.booking_service = booking_service
        self.room_service = booking_service.room_service
        self.user_service = booking_service.user_service
        self.view = view

    # TODO add data validation
    def book_room(self):
        """
        Orchestrates data flow from view to booking services and vice versa to book room.
        Returns room booking status.

        :return: True or False
        """
        all_rooms = self.room_service.get_all_rooms()
        all_users = self.user_service.get_all_users()

        self.view.display_greetings()
        self.view.display_all_rooms(all_rooms)
        self.view.display_all_users(all_users)

        [user_id, room_id, date, start_time, end_time] = self.view.get_user_input()
        unix_start_time = to_unix(date, start_time)
        unix_end_time = to_unix(date, end_time)

        success, result = self.booking_service.book_room(user_id, room_id, [unix_start_time, unix_end_time])
        if success:
            self.view.display_success_message(result)
            return True
        else:
            overlapping_bookings = self.convert_bookings_to_human_readable_format(result)
            self.view.display_fail_message(overlapping_bookings)
            return False

    def convert_bookings_to_human_readable_format(self, bookings):
        """
        Converts all ids in Booking object to human-readable format.

        :param bookings: list of Booking objects
        :return: list of Booking information strings
        """
        human_readable_bookings = []
        for booking in bookings:
            user = self.booking_service.get_user_from_booking(booking)
            room = self.booking_service.get_room_from_booking(booking)
            date = get_date(booking.unix_datetime_start)
            time_start = get_time(booking.unix_datetime_start)
            time_end = get_time(booking.unix_datetime_end)
            human_readable_bookings.append(
                f"Booking #{booking.booking_id}. Room # {room.number}. Time: {date} {time_start} - {time_end}. Booked by {user}")

        return human_readable_bookings
