import sqlite3

def create_database():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    return connection, cursor

def create_users_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER,
    name TEXT, 
    email TEXT
    )
    """)

def add_user(cursor, user_id, name, email):
    cursor.execute(
    "INSERT INTO users (id, name,email) VALUES (?, ?, ?)",
    (user_id, name, email)
    )

def get_user(cursor, user_id):
    cursor.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    )
    user = cursor.fetchone()
    return user