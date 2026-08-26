import sqlite3

# create and insert data into table

# connection = sqlite3.connect("employees.db")
# cursor = connection.cursor()
# with open("sql_practice.sql", "r") as file:
#     sql_script = file.read()
# cursor.executescript(sql_script)


# fetch all data

# connection = sqlite3.connect("employees.db")
# cursor = connection.cursor()
# cursor.execute("SELECT * FROM employees")
# employees = cursor.fetchall()
# for employee in employees:
#     print(employee)

# fetch one data

# connection = sqlite3.connect("employees.db")
# cursor = connection.cursor()
# cursor.execute("SELECT * FROM employees")
# employee = cursor.fetchone()
# print(employee)

# conditional fetch

# connection = sqlite3.connect("employees.db")
# cursor = connection.cursor()
# name = "Khushboo"

# cursor.execute(
#     f"SELECT * FROM employees WHERE name = '{name}'"
# )

# employees = cursor.fetchall()
# for employee in employees:
#     print(employee)

# fetch many

# connection = sqlite3.connect("employees.db")
# cursor = connection.cursor()
# cursor.execute("SELECT * FROM employees")
# employees = cursor.fetchmany(2)
# for employee in employees:
#     print(employee)

# update a record

# connection = sqlite3.connect("employees.db")
# cursor = connection.cursor()
# cursor.execute("""
#     UPDATE employees
#     SET salary = ?
#     WHERE id = ?
# """, (55000, 1))

# connection = sqlite3.connect("employees.db")
# cursor = connection.cursor()
# cursor.execute("""
#     SELECT *
#     FROM employees
#     WHERE id = ?
# """, (1,))
# employee = cursor.fetchone()
# print(employee)

# delete data

# connection = sqlite3.connect("employees.db")
# cursor = connection.cursor()
# cursor.execute("""
#     DELETE FROM employees
#     WHERE id = ?
# """, (2,))

connection = sqlite3.connect("employees.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM employees")
employees = cursor.fetchall()
for employee in employees:
    print(employee)
    

connection.commit()
connection.close()