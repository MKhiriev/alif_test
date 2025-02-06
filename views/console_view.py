from utils.date_time import from_unix

# noinspection PyMethodMayBeStatic
class ConsoleView:

    def display_all_rooms(self, all_room_numbers):
        print(f"=================")
        print(f"Available rooms: ")
        for room in all_room_numbers:
            print(room)
        print(f"=================")

    def display_all_users(self, all_users):
        print(f"=================")
        print(f"Available users: ")
        for user in all_users:
            print(user)
        print(f"=================")

    # noinspection PyMethodMayBeStatic
    def display_success_message(self, registered_booking):
        print(f"Created new booking. Details below: "
              f"{registered_booking}")

    def display_fail_message(self, overlapping_bookings):
        print("Failed to create booking. Choose another time. "
              "Your booking is overlapping with booking(s) below:")
        for booking in overlapping_bookings:
            print(booking)

    def update_view(self):
        self.clear_console()

    def display_greetings(self):
        print("Hello! This program is designed to book rooms")

    def get_user_input(self):
        user_id = input("Who will book room? Enter user ID: ")
        room_id = input("Which room would you like? Enter room ID: ")
        date = input("Enter date (DD.MM.YYYY): ")
        start_time = input("Enter start time (HH:MM): ")
        end_time = input("Enter end time (HH:MM): ")

        return [user_id, room_id, date, start_time, end_time]

    # TODO написать для всех ОС
    def clear_console(self):
        pass
