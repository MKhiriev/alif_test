import sqlite3

from models.booking import Booking


class BookingRepository:
    def __init__(self, database):
        self.database = database

    def get_all_bookings(self):
        """
        Returns all bookings.
        
        :return: list of all Bookings
        """
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        bookings_info_query = "SELECT * FROM bookings"
        cursor.execute(bookings_info_query)

        bookings_data = cursor.fetchall()
        conn.close()

        return [Booking(*booking_data) for booking_data in bookings_data]

    def get_booking_by_id(self, booking_id):
        """
        Returns Booking by id.

        :param booking_id: id of booking
        :return: Booking
        """
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        booking_info_query = f"SELECT * FROM bookings WHERE booking_id = {booking_id}"
        cursor.execute(booking_info_query)

        found_booking_info = cursor.fetchone()
        conn.close()

        if found_booking_info:
            return Booking(*found_booking_info)
        else:
            return None

    def get_bookings_by_room_id_and_booking_time(self, room_id, booking_time):
        """
        SELECTs from Database room bookings based on room and given booking time range.

        :param room_id: id of room which is going to be booked
        :param booking_time: list with two elements [datetime_start, datetime_end]
        :return: list of found bookings
        """
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        [unix_booking_start_time, unix_booking_end_time] = booking_time
        find_booking_by_start_end_time_query = (f"SELECT * FROM bookings WHERE room_id = {room_id} AND "
                                                f"("
                                                f"({unix_booking_start_time} BETWEEN unix_datetime_start AND unix_datetime_end) "
                                                f"OR ({unix_booking_end_time} BETWEEN unix_datetime_start AND unix_datetime_end) "
                                                f"OR (unix_datetime_start BETWEEN {unix_booking_start_time} AND {unix_booking_end_time}) "
                                                f"OR (unix_datetime_end BETWEEN {unix_booking_start_time} AND {unix_booking_end_time})"
                                                f")")
        cursor.execute(find_booking_by_start_end_time_query)
        found_bookings_data = cursor.fetchall()
        conn.close()

        return [Booking(*booking_data) for booking_data in found_bookings_data]

    def get_bookings_by_room_id(self, room_id):
        """
        Returns Bookings list by room id.

        :param room_id: id of room
        :return: list of Bookings
        """
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        find_bookings_by_room_id = f"SELECT * FROM bookings WHERE room_id = {room_id}"

        cursor.execute(find_bookings_by_room_id)
        found_bookings_data = cursor.fetchall()
        conn.close()

        return [Booking(*booking_data) for booking_data in found_bookings_data]

    def add_room_booking(self, user_id, room_id, booking_time):
        """
        Adds room booking to the database.

        :param user_id: id of user who is going to book
        :param room_id: id of room which is going to be booked
        :param booking_time: list with two elements [datetime_start, datetime_end]
        :return: Booking object
        """
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        [unix_booking_start_time, unix_booking_end_time] = booking_time
        add_booking_query = (f"INSERT INTO bookings (user_id, room_id, unix_datetime_start, unix_datetime_end) "
                             f"VALUES ({user_id}, {room_id}, {unix_booking_start_time}, {unix_booking_end_time})")

        cursor.execute(add_booking_query)
        added_booking_id = cursor.lastrowid
        booking_data = [added_booking_id, user_id, room_id, unix_booking_start_time, unix_booking_end_time]

        conn.commit()
        conn.close()

        return Booking(*booking_data)
