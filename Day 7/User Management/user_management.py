users = [
    {
        "id": 1,
        "username": "asaf",
        "email": "asaf@example.com",
        "active": True
    },
    {
        "id": 2,
        "username": "amit",
        "email": "amit@example.com",
        "active": True
    },
    {
        "id": 3,
        "username": "david",
        "email": "david@example.com",
        "active": False
    }
]

def find_user(username):
    for user in users:
        if user["username"] == username:
            return user
    return None

def get_active_users():
    active_users = []
    for user in users:
        if user["active"]:
            active_users.append(user)
    return active_users

def add_user(id, username, email, active=True):
    new_user = {
        "id": id,
        "username": username,
        "email": email,
        "active": active
    }
    users.append(new_user)
    return new_user