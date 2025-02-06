import sqlite3
from models.room import Room

class RoomRepository:
    def __init__(self, database):
        self.database = database

    def get_all_rooms(self):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        all_rooms_info_query = "SELECT * FROM rooms"
        cursor.execute(all_rooms_info_query)

        rooms_data = cursor.fetchall()
        conn.close()

        return [Room(*room_data) for room_data in rooms_data]

    def get_room_by_id(self, room_id):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        room_info_query = f"SELECT * FROM rooms WHERE room_id = {room_id}"
        cursor.execute(room_info_query)

        found_room_info = cursor.fetchone()
        conn.close()
        if found_room_info:
            return Room(*found_room_info)
        else:
            return None

    # TODO добавить CRUD методы