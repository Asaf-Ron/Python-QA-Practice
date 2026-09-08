import requests

def get_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url, timeout=10)
    return response.status_code, response.json()

def get_user_data(user_id):
    status_code, user = get_user(user_id)
    return user


