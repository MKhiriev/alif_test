class RoomService:
    def __init__(self, room_repository):
        self.room_repository = room_repository

    def get_all_rooms(self):
        return self.room_repository.get_all_rooms()

    def get_room_by_id(self, room_id):
        return self.room_repository.get_room_by_id(room_id)
