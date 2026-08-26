import configparser

config = configparser.ConfigParser()
config.read("config.ini")

print(config["database"]["host"])
print(config.getint("database", "port"))
print(config["application"]["name"])
print(config.getboolean("application", "debug"))

if "database" in config:
    print("Database configuration exists")

if "host" in config["database"]:
    print("Host is configured")

# add
config["database"]["timeout"] = "30"

# edit
config["application"]["debug"] = "false"

# add new section
config["logging"] = {
    "level": "INFO",
    "file": "app.log"
}

with open("config_updated.ini", "w") as file:
    config.write(file)


import configparser

config = configparser.ConfigParser()
files = config.read("config.ini")
if not files:
    print("Config file not found!")

print(config["database"]["host"])
print(config.getint("database", "port"))
print(config["application"]["name"])
print(config.getboolean("application", "debug"))

config["database"]["host"] = "production-db"
config["application"]["debug"] = "false"
config["database"]["timeout"] = "30"
config["logging"] = {
    "level": "INFO",
    "file": "application.log"
}
with open("config.ini", "w") as file:
    config.write(file)
