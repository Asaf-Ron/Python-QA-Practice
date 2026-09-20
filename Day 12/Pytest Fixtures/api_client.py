import requests

def get_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url, timeout=10)
    return response


