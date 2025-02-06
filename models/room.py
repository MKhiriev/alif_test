class Room:
    def __init__(self, room_id, number):
        self.room_id = room_id
        self.number = number

    def __str__(self):
        return f"ID: {self.room_id}, Number: {self.number}"

    # TODO добавить геттеры и сеттеры
    # TODO добавить @property для валидации значений
