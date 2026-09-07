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

df = df[['name', 'email', 'phone', 'address.city', 'company.name']]