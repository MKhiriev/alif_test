import sqlite3


def create_tables(cursor):
    """
    Create tables in database.

    :param cursor: sqlite3.Cursor object
    :return: None
    """
    pass


def insert_data(cursor):
    """
    Insert testing data in database.

    :param cursor: sqlite3.Cursor object
    :return: None
    """
    pass


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