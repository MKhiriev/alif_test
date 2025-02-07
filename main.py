""" TASK
Онлайн-тест "New task for middle/senior Python developer"
1. Задача: В офисе есть 5 кабинетов. Не используя фреймворки, написать команду, которая проверяет свободен ли кабинет в определенное время и даст возможность его забронировать.
После бронирования кабинета, чтоб была команда — Отправлять уведомление человеку, который занимает его (на Email и номер телефона) с датой, временем и номером кабинета.
Если кабинет занят, выводить сообщение кем и до скольки он занят.

Использовать СУБД.
Желательно использовать РЕР-стандарты.
Во время разработки используйте git и Github и делайте значимые коммиты.
Результаты задачи должны быть размещены в вашей учетной записи Github, отправьте нам только ссылку.
Мы не принимаем результаты задач в .zip/.rar и т. д.
"""
import sqlite3

from database_utils import prepare_db, flush_db
from datetime_utils import to_unix, from_unix
from models.booking import Booking
from models.user import User


# TODO move string 'example.db' from method to single place
def get_booking_info(room_id, booking_time):
    """
    SELECTs from Database room bookings based on room and given booking time range.

    :param room_id: id of room which is going to be booked
    :param booking_time: list with two elements [datetime_start, datetime_end]
    :return: list of found bookings
    """
    conn = sqlite3.connect('example.db')
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


def check_if_available(room_id, booking_time):
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
    overlapping_bookings = get_booking_info(room_id, booking_time)

    if not overlapping_bookings:
        return [room_is_available, no_overlapping_bookings]
    else:
        return [room_is_not_available, overlapping_bookings]


# TODO move string 'example.db' from method to single place
def add_room_booking(user_id, room_id, booking_time):
    """
    Adds room booking to the database.

    :param user_id: id of user who is going to book
    :param room_id: id of room which is going to be booked
    :param booking_time: list with two elements [datetime_start, datetime_end]
    :return: Booking object
    """
    [unix_booking_start_time, unix_booking_end_time] = booking_time
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    add_booking_query = (f"INSERT INTO bookings (user_id, room_id, unix_datetime_start, unix_datetime_end) "
                         f"VALUES ({user_id}, {room_id}, {unix_booking_start_time}, {unix_booking_end_time})")

    cursor.execute(add_booking_query)
    added_booking_id = cursor.lastrowid
    booking_data = [added_booking_id, user_id, room_id, unix_booking_start_time, unix_booking_end_time]

    conn.close()

    return Booking(*booking_data)


# TODO move string 'example.db' from method to single place
def get_user_info(user_id):
    """
    Get user info.

    :param user_id: id of user who is going to book
    :return: list of user info [user_id, name, email, telephone]
    """
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    user_info_query = f"SELECT * FROM users WHERE user_id = {user_id}"
    cursor.execute(user_info_query)

    found_user_info = cursor.fetchone()
    conn.close()

    if found_user_info:
        return User(*found_user_info)
    else:
        return None


def send_booking_info_email(user_email, booking):
    """
    Sends email with booking info.

    :param user_email: email address of user
    :param booking: Booking object
    :return: None
    """
    print(f"Sending email to {user_email}..."
          f"{booking}")


def send_booking_info_sms(user_telephone, booking):
    """
    Sends sms with created booking info.

    :param user_telephone: telephone number of user
    :param booking: Booking object
    :return: None
    """
    print(f"Sending sms to {user_telephone}..."
          f"{booking}")


def notify_user(user_id, booking):
    """
    Notifies user with info about created booking.

    :param user_id: id of user who is going to book
    :param booking: Booking object
    :return: None
    """
    user = get_user_info(user_id)
    user_email = user.email
    user_telephone = user.telephone

    send_booking_info_email(user_email, booking)
    send_booking_info_sms(user_telephone, booking)


def print_booking_info(booking):
    """
    Prints booking info to the user.

    :param booking: Booking object
    :return: None
    """
    user_id = booking.user_id
    room_id = booking.room_id
    user_name = get_user_info(user_id).name
    datetime_start = booking.unix_datetime_start
    datetime_end = booking.unix_datetime_end
    date = from_unix(datetime_start)['date']
    time_start = from_unix(datetime_start)['time']
    time_end = from_unix(datetime_end)['time']

    print(f'Booking details: {room_id} | {date} {time_start}-{time_end} | {user_name}')


def book_room(user_id, room_id, booking_time):
    """
    Books a room.

    :param user_id: id of user who is going to book
    :param room_id: id of room which is going to be booked
    :param booking_time: list with two elements [datetime_start, datetime_end]
    :return: None
    """
    # Check if room available. Use room number and booking time (start, end).
    [available, overlapping_bookings] = check_if_available(room_id, booking_time)
    # if room is available then add booking and notify person by email and phone number
    if available:
        new_booking = add_room_booking(user_id, room_id, booking_time)
        notify_user(user_id, new_booking)
    # else if room is not available - show booking failed message. Show existing bookings: who booked + booking time
    else:
        print('Room is already booked. Choose another time.')
        for booking in overlapping_bookings:
            print_booking_info(booking)


if __name__ == '__main__':
    database = 'example.db'
    prepare_db(database)

    room_number = input('Choose desired room number: ')
    booking_date = input('Write desired date in given format [DD.MM.YYYY]: ')
    booking_time_start = input('Starting time in given format [HH:MM]: ')
    booking_time_end = input('Ending time in given format [HH:MM]: ')
    user_id = input('Choose who is going to book room: ')

    unix_booking_time_start = to_unix(booking_date, booking_time_start)
    unix_booking_time_end = to_unix(booking_date, booking_time_end)

    print('Checking if room is available...')

    book_room(user_id, room_number, [unix_booking_time_start, unix_booking_time_end])

    flush_db(database)
