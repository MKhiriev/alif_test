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


def check_if_available(room_id, booking_time):
    """
    Checks room availability by booking time.

    :param room_id: id of room which is going to be booked
    :param booking_time: list with two elements [datetime_start, datetime_end]
    :return: list with two elements - [if_available, overlapping_bookings]
    """
    pass


def add_room_booking(user_id, room_id, booking_time):
    """
    Adds room booking to the database.

    :param user_id: id of user who is going to book
    :param room_id: id of room which is going to be booked
    :param booking_time: list with two elements [datetime_start, datetime_end]
    :return: booking id of added booking
    """
    pass


def notify_user(user_id, booking_info):
    """
    Notifies user with info about created booking.

    :param user_id: id of user who is going to book
    :param booking_info: booking info which is going to be printed
    :return: None
    """
    pass


def print_booking_info(booking):
    """
    Prints booking info to the user.

    :param booking: booking information which is going to be printed
    :return: None
    """
    pass


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
        booking_info = add_room_booking(user_id, room_id, booking_time)
        notify_user(user_id, booking_info)
    # else if room is not available - show booking failed message. Show existing bookings: who booked + booking time
    else:
        print('Room is already booked. Choose another time.')
        for booking in overlapping_bookings:
            print_booking_info(booking)
