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

""" System Objects and Their Properties """
"""
User is attached to Booking. Also Room is attached to Booking. Another Booking details are booking start time and booking end time.
In relational DBs we attach other objects via their IDs.
Booking:
    - booking_id (INTEGER)
    - user_id (INTEGER)
    - room_id (INTEGER)
    - start_time (depending on database DATETIME or INTEGER)
    - end_time (depending on database DATETIME or INTEGER)

User object has following info: user id, name, Email, Telephone number. 
Telephone number is in Tajikistan's format (13 characters).
User:
    - user_id (INTEGER)
    - name (depending on database TEXT of VARCHAR)
    - email (depending on database TEXT of VARCHAR)
    - telephone (depending on database TEXT of VARCHAR with size 13)
    
Room object only has a room number.
Room:
    - room_id (INTEGER)
    - number (INTEGER)
"""

def book_room():
    # Check if room available. Use room number and booking time (start, end).
    # if room is available then add booking and notify person by email and phone number
    # else if room is not available - show booking failed message. Failed message: who booked + booking time
    pass

