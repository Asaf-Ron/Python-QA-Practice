import requests

def get_user_from_api(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url, timeout=10)

    return response.json()

user = get_user_from_api(1)
print(user["id"])
print(user["name"])
print(user["email"])