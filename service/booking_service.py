class BookingService:
    def __init__(self, booking_repository, user_service, room_service, notification_service):
        self.booking_repository = booking_repository
        self.user_service = user_service
        self.room_service = room_service
        self.notification_service = notification_service

    def book_room(self, user_id, room_id, unix_booking_start_time, unix_booking_end_time):
        booking_success = True
        booking_fail = False

        [available, overlapping_bookings] = self.check_if_available(room_id, unix_booking_start_time, unix_booking_end_time)
        if available:
            registered_booking = self.booking_repository.add_room_booking(user_id, room_id, unix_booking_start_time, unix_booking_end_time)
            self.notification_service.notify_user(user_id, f"Created new booking. Details below: "
                                                           f"{registered_booking}")
            return [booking_success, registered_booking]
        if not available:
            return [booking_fail, overlapping_bookings]

    def check_if_available(self, room_id, unix_booking_start_time, unix_booking_end_time):
        room_is_available = True
        room_is_not_available = False

        no_overlapping_bookings = []
        overlapping_bookings = self.booking_repository.get_bookings_by_room_id_and_booking_time(room_id, unix_booking_start_time, unix_booking_end_time)

        if not overlapping_bookings:
            return [room_is_available, no_overlapping_bookings]
        else:
            return [room_is_not_available, overlapping_bookings]

    def get_user_from_booking(self, booking):
        user_id = booking.user_id
        return self.user_service.get_user_by_id(user_id)

    def get_room_from_booking(self, booking):
        room_id = booking.room_id
        return self.room_service.get_room_by_id(room_id)