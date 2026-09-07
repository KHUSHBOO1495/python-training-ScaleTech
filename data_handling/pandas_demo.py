import pandas as pd

data = {
    "name": ["Khushboo", "Payal", "Tejasvi", "Preksha"],
    "age": [21, 22, 25, 26],
    "department": ["IT", "HR", "IT", "Finance"],
    "salary": [50000, 60000, 55000, 45000]
}

df = pd.DataFrame(data)
print(df)
print(df['name'])
print(df[['name','salary']])
print("--------")
print(df.loc[0])
print("--------")
print(df.loc[2])
print("--------")
print(df.loc[0:2])
print("--------")
print(df.iloc[0])
print("--------")
print(df.iloc[2])
print("--------")
print(df.iloc[0:2])
print("--------")
print(df.head(2))
print(df.tail())
print(df.info)
print("--------")
print(df.info())
print(df.describe())
print(df['salary'].mean())
print(df['salary'].max())
print(df['salary'].min())
print(df['salary'].sum())
print(df['name'].count())
print(df.shape)
print(df.columns)
print(df.dtypes)

print("----Filtering data----")
result = df[df["salary"] > 50000]
print(result)

df[
    (df["department"] == "IT") &
    (df["salary"] > 45000)
]

df["bonus"] = df["salary"] * 0.10

df.sort_values("salary")
df.sort_values("salary", ascending=False)