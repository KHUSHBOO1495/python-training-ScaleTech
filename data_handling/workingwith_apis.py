import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
print(response.status_code)
data = response.json()
print(type(data))
print(type(data[0]))
print(data[0].keys())
print(data[0])

df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df.columns)
print(df[['name', 'email', 'phone']])

df = pd.json_normalize(data)
print(df)
print(df.columns)
print(df['address.city'])

data = df[['name', 'email', 'phone', 'address.city', 'company.name']]


# -----------------------------------------------------

url = "https://jsonplaceholder.typicode.com/users"
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    df = pd.json_normalize(data)
    print(len(df)) # print(df['name'].count())
    print(df.shape)
    print(df.columns)
    print(df[['name', 'email', 'phone', 'address.city', 'company.name']])
    print(df[df['address.city'] == 'South Christy'])
    print(df.groupby('address.city')['name'].count())
    df.to_csv("users_api_data.csv", index=False)

except requests.exceptions.RequestException as e:
    print("API request failed:", e)