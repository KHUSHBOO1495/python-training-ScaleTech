import requests

response = requests.get("https://example.com")

print("Status code: ", response.status_code)
print("URL: ", response.url)
print("Response: ", response.text)
print("Content-Type: ", response.headers['Content-Type'])  # response.headers.get("Content-Type")



url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 2,
    "id": 11
}

response = requests.get(url, params=params)
data = response.json()

print(type(data))
print(data[0]["title"])


try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    print(data[0]["title"])

except requests.RequestException as e:
    print("Request failed:", e)




url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Python Web Scraping",
    "body": "I am learning Python web scraping.",
    "userId": 5
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
print(response.json()['id'])