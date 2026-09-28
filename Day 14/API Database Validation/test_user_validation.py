import pytest

from api_client import get_user_from_api
from database import create_database, create_users_table, add_user, get_user

@pytest.fixture
def database():
    connection, cursor = create_database()

    create_users_table(cursor)

    add_user(
        cursor,
        1,
        "Leanne Graham",
        "Sincere@april.biz"
    )

    yield cursor
    connection.close()

def test_api_user_matches_database(database):
    api_user = get_user_from_api(1)
    db_user = get_user(database,1)

    assert api_user["id"] == db_user[0]
    assert api_user["name"] == db_user[1]
    assert api_user["email"] == db_user[2]