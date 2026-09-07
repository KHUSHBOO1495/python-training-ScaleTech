import pandas as pd

data = {
    "Name": ["Khushboo", "Payal", "Tejasvi", "Neha", "Khushboo", "Preksha"],
    "Age": [25, None, 22, 30, 25, None],
    "Department": ["IT", "HR", "IT", "sales", "IT", "HR"],
    "Salary": [50000, 45000, None, 60000, 50000, 48000]
}

df = pd.DataFrame(data)

print(df)
df.isnull()
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
# df["Age"] = df["Age"].fillna(0)

# df["Age"] = df["Age"].fillna(0)  # check duplicate
print(df.duplicated().sum())     # count duplicate
df = df.drop_duplicates()        # remove duplicate

print(df.dtypes)
df["Age"] = df["Age"].astype(int)

print(df)

print(df.groupby("Department")["Salary"].mean())
print(df.groupby("Department")["Salary"].sum())
print(df.groupby("Department")["Salary"].max())
print(df.groupby("Department")["Name"].count())

print(df.groupby("Department")["Salary"].agg(["mean", "min", "max", "count"]))