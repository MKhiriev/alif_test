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
