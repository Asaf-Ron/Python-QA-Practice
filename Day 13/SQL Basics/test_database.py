import pytest
import sqlite3

from database import create_users_table, add_user, get_user

@pytest.fixture
def database():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    create_users_table(cursor)

    yield connection, cursor
    
    connection.close()

def test_add_and_get_user(database):
    connection, cursor = database
    add_user(cursor, 1, "Asaf", "asaf@example.com")

    user = get_user(cursor, 1)
    assert user[0] == 1
    assert user[1] == "Asaf"
    assert user[2] == "asaf@example.com"

def test_get_nonexistent_user(database):
    connection, cursor = database

    user = get_user(cursor, 999)
    assert user is None