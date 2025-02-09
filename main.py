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
from controllers.booking_controller import BookingController
from repositories.booking_repository import BookingRepository
from repositories.room_repository import RoomRepository
from repositories.user_repository import UserRepository
from services.booking_service import BookingService
from services.room_service import RoomService
from services.user_notification_service import UserNotificationService

from services.user_service import UserService
from utils.database_utils import prepare_db, flush_db
from utils.notifiers.email_notifier import EmailNotifier
from utils.notifiers.sms_notifier import SmsNotifier
from views.console_view import ConsoleView

database = 'example.db'
user_repo = UserRepository(database)
booking_repo = BookingRepository(database)
room_repo = RoomRepository(database)

sms_notifier = SmsNotifier('Babilon-M')
email_notifier = EmailNotifier('Gmail.com')

user_service = UserService(user_repo)
room_service = RoomService(room_repo)
notification_service = UserNotificationService(sms_notifier, email_notifier, user_service)
booking_service = BookingService(booking_repo, user_service, room_service, notification_service)

view = ConsoleView()

booking_controller = BookingController(booking_service, view)

if __name__ == '__main__':
    database = 'example.db'
    prepare_db(database)

    success = False
    while not success:
        success = booking_controller.book_room()

    flush_db(database)
