class ConsoleView:

    def get_user_input(self):
        """
        Gets user input for booking room.

        :return: list of booking information
        """
        user_id = input("Who will book room? Enter user ID: ")
        room_id = input("Which room would you like? Enter room ID: ")
        date = input("Enter date (DD.MM.YYYY): ")
        start_time = input("Enter start time (HH:MM): ")
        end_time = input("Enter end time (HH:MM): ")

        return [user_id, room_id, date, start_time, end_time]

    def display_all_rooms(self, all_rooms):
        """
        Displays in console all existing room numbers.

        :param all_rooms: list of Room objects
        :return: None
        """
        print(f"=================")
        print(f"Available rooms: ")
        for room in all_rooms:
            print(room)
        print(f"=================")

    def display_all_users(self, all_users):
        """
        Displays in console all existing users.

        :param all_users: list of Users
        :return: None
        """
        print(f"=================")
        print(f"Available users: ")
        for user in all_users:
            print(user)
        print(f"=================")

    def display_success_message(self, registered_booking):
        """
        Displays in console success message that booking was registered.

        :param registered_booking: Booking object
        :return: None
        """
        print(f"Created new booking. Details below: "
              f"{registered_booking}")

    def display_fail_message(self, overlapping_bookings):
        """
        Displays in console message that booking process is failed.

        :param overlapping_bookings: list of Booking objects that overlap with suggested booking.
        :return: None
        """
        print("Failed to create booking. Choose another time. "
              "Your booking is overlapping with booking(s) below:")
        for booking in overlapping_bookings:
            print(booking)

    def display_greetings(self):
        """
        Displays in console greetings.

        :return: None
        """
        print("Hello! This program is designed to book rooms")
