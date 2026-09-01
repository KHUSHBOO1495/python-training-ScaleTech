import requests


def get_user_name(user_id):
    url = f"https://example.com/users/{user_id}"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    breakpoint()

    return data["name"]


def create_greeting(user_id):
    name = get_user_name(user_id)

    return f"Hello, {name}!"
