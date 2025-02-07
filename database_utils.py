import sqlite3


def create_tables(cursor):
    """
    Create tables in database.

    :param cursor: sqlite3.Cursor object
    :return: None
    """
    create_user_table_query = ("CREATE TABLE IF NOT EXISTS users "
                               "(user_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, telephone VARCHAR(13))")
    create_room_table_query = ("CREATE TABLE IF NOT EXISTS rooms "
                               "(room_id INTEGER PRIMARY KEY AUTOINCREMENT, number INT)")
    create_booking_table_query = ("CREATE TABLE IF NOT EXISTS bookings "
                                  "(booking_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, room_id INTEGER, unix_datetime_start INTEGER, unix_datetime_end INTEGER)")

    cursor.execute(create_user_table_query)
    cursor.execute(create_room_table_query)
    cursor.execute(create_booking_table_query)


def insert_data(cursor):
    """
    Insert testing data in database.

    :param cursor: sqlite3.Cursor object
    :return: None
    """
    insert_users_data_query = ("INSERT INTO users (user_id, name, email, telephone) VALUES "
                               "(0, 'Rasul', 'khiriev.rasul@inbox.ru', '+992989991745'), "
                               "(1, 'Johnybek', 'johny@mail.com', '+992989661777'), "
                               "(2, 'Maher', 'ikitboss@gmail.com', '+992666771779')")
    insert_room_data_query = ("INSERT INTO rooms (room_id, number) VALUES "
                              "(0, 1), "
                              "(1, 2), "
                              "(2, 3), "
                              "(3, 4), "
                              "(4, 5)")
    insert_booking_data_query = (
        "INSERT INTO bookings (user_id, room_id, unix_datetime_start, unix_datetime_end) VALUES "
        "(0, 1, 1738936800, 1738940400), "  # Fri Feb 07 2025 19:00:00 - 20:00:00
        "(2, 1, 1738933200, 1738935000), "  # Fri Feb 07 2025 18:00:00 - 18:30:00
        "(1, 3, 1739091600, 1739093400), "  # Sun Feb 09 2025 14:00:00 - 14:30:00
        "(1, 2, 1740805200, 1740812400)")  # Sat Mar 01 2025 10:00:00 - 12:00:00

    cursor.execute(insert_users_data_query)
    cursor.execute(insert_room_data_query)
    cursor.execute(insert_booking_data_query)


def prepare_db():
    """
    Prepares database for booking app.

    :return: None
    """
    # 1. establish database connection
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # 2. create tables
    create_tables(cursor)
    # 3. insert test data
    insert_data(cursor)

    # 4. commit changes
    conn.commit()
    # 5. close database connection
    conn.close()