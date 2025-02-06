import sqlite3

from models.user import User

class UserRepository:
    db = 'example.db'

    def __init__(self, database):
        self.database = database

    def get_user_by_id(self, user_id):
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
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        user_info_query = "SELECT * FROM users"
        cursor.execute(user_info_query)

        users_data = cursor.fetchall()
        conn.close()

        return [User(*user_data) for user_data in users_data]

    def get_contact_info_by_user_id(self, user_id):
        user = self.get_user_by_id(user_id)
        return user.get_contact_info()


    # TODO добавить CRUD методы