import sqlite3

from models.user import User


class UserRepository:
    def __init__(self, database):
        self.database = database

    def get_user_by_id(self, user_id):
        """
        Get user info.

        :param user_id: id of user who is going to book
        :return: list of user info [user_id, name, email, telephone]
        """
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        user_info_query = f"SELECT * FROM users WHERE user_id = {user_id}"
        cursor.execute(user_info_query)

        found_user_info = cursor.fetchone()
        conn.close()

        if found_user_info:
            return User(*found_user_info)
        else:
            return None

    def get_all_users(self):
        """
        Get all users.

        :return: list of all Users
        """
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        user_info_query = "SELECT * FROM users"
        cursor.execute(user_info_query)

        users_data = cursor.fetchall()
        conn.close()

        return [User(*user_data) for user_data in users_data]

    def get_contact_info_by_user_id(self, user_id):
        """
        Get contact info of selected user.

        :param user_id: id of user
        :return: tuple with telephone and email
        """
        user = self.get_user_by_id(user_id)
        return user.get_contact_info()
