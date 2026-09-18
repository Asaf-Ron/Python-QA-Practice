import requests
def create_post(title, body, user_id):
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }

    response = requests.post(
        url,
        json= payload, 
        timeout=10
        )

    return response

def create_post_from_data(post_data):
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.post(
        url,
        json=post_data,
        timeout=10
    )

    return response