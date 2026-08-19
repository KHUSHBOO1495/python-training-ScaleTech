import os

print(os.getcwd()) # current working directory

print(os.listdir()) # list files and directories 
# os.listdir("data") -> specify the directory

api_key = os.environ.get("API_KEY") 
# OR
os.getenv("API_KEY")

path = os.path.join("python", "data.csv")
print(path)
os.path.exists(path)
os.path.isfile(path)
os.path.isdir(path)

# example
if os.path.exists("employees.csv"):
    print("File exists")
else:
    print("File does not exist")


size = os.path.getsize("math-module.py")
print(size)

os.mkdir("reports")
os.rmdir("reports")

path = "/company/data/report.csv"

print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.splitext(path))
print(os.path.abspath(path))