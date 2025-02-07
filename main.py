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

from repositories.booking_repository import BookingRepository
from repositories.room_repository import RoomRepository
from repositories.user_repository import UserRepository
from services.booking_service import BookingService
from services.user_notification_service import UserNotificationService

from services.user_service import UserService
from utils.database_utils import prepare_db, flush_db
from utils.datetime_utils import to_unix, from_unix
from utils.notifiers.email_notifier import EmailNotifier
from utils.notifiers.sms_notifier import SmsNotifier

database = 'example.db'
user_repo = UserRepository(database)
booking_repo = BookingRepository(database)
room_repo = RoomRepository(database)

sms_notifier = SmsNotifier('Babilon-M')
email_notifier = EmailNotifier('Gmail.com')

user_service = UserService(user_repo)
notification_service = UserNotificationService(sms_notifier, email_notifier, user_service)
booking_service = BookingService(booking_repo, notification_service)


def print_booking_info(booking):
    """
    Prints booking info to the user.

    :param booking: Booking object
    :return: None
    """
    user_id = booking.user_id
    room_id = booking.room_id
    user_name = user_repo.get_user_by_id(user_id).name
    datetime_start = booking.unix_datetime_start
    datetime_end = booking.unix_datetime_end
    date = from_unix(datetime_start)['date']
    time_start = from_unix(datetime_start)['time']
    time_end = from_unix(datetime_end)['time']

    print(f"Booking details: [{room_id} | {date} {time_start}-{time_end} | {user_name}]")


def get_user_input():
    global room_number, user_id, unix_booking_time_start, unix_booking_time_end
    room_number = input('Choose desired room number: ')
    booking_date = input('Write desired date in given format [DD.MM.YYYY]: ')
    booking_time_start = input('Starting time in given format [HH:MM]: ')
    booking_time_end = input('Ending time in given format [HH:MM]: ')
    user_id = input('Choose who is going to book room: ')
    unix_booking_time_start = to_unix(booking_date, booking_time_start)
    unix_booking_time_end = to_unix(booking_date, booking_time_end)

    return room_number, user_id, unix_booking_time_start, unix_booking_time_end


if __name__ == '__main__':
    database = 'example.db'
    prepare_db(database)

    [user_id, room_number, unix_booking_time_start, unix_booking_time_end] = get_user_input()

    print('Checking if room is available...')

    booking_service.book_room(user_id, room_number, [unix_booking_time_start, unix_booking_time_end])

    flush_db(database)
