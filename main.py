from controllers.booking_controller import BookingController
from repository.booking_repository import BookingRepository
from repository.room_repository import RoomRepository
from repository.user_repository import UserRepository
from service.booking_service import BookingService
from service.notification_service import NotificationService
from service.room_service import RoomService
from service.user_service import UserService
from utils.notifiers.email_notifier import EmailNotifier
from utils.notifiers.sms_notifier import SmsNotifier
from views.console_view import ConsoleView

if __name__ == '__main__':
    example_db = 'example.db'
    room_repository = RoomRepository('example.db')
    booking_repository = BookingRepository('example.db')
    user_repository = UserRepository('example.db')
    user_service = UserService(user_repository)
    room_service = RoomService(room_repository)
    sms_notifier = SmsNotifier("Babilon-M")
    email_notifier = EmailNotifier("GMail")
    notification_service = NotificationService(sms_notifier, email_notifier, user_service)
    booking_service = BookingService(booking_repository, user_service, room_service, notification_service)
    view = ConsoleView()

    booking_controller = BookingController(booking_service, view)
    success = False

    while not success:
        success = booking_controller.book_room()
