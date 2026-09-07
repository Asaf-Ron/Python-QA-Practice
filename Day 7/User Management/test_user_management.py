from user_management import find_user, get_active_users, add_user

def test_find_existing_user():
    result = find_user("asaf")
    assert result["username"] == "asaf", f"Expected username to be asaf but got {result['username']}"

def test_find_missing_user():
    result = find_user("nonexistent")
    assert result is None, f"Expected result to be None but got {result}"

def test_get_active_users():
    result = get_active_users()
    assert len(result) == 2, f"Expected 2 active users but got {len(result)}"
    assert all(user["active"] for user in result), "Expected all users to be active"

def test_no_inactive_users():
    result = get_active_users()
    assert all(user["active"] for user in result), "Expected no inactive users in the result"

def test_add_user():
    new_user = add_user(4, "newuser", "newuser@example.com", True)
    assert new_user["username"] == "newuser", f"Expected username to be newuser but got {new_user['username']}"