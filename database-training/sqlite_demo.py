import sqlite3
from employee import Employee

connection = sqlite3.connect('employee.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
               first text,
               last text,
               amount integer
               )""")


def insert_emp(emp):
    with connection:
        cursor.execute("INSERT INTO employees VALUES (:first, :last, :amount)", {'first': emp.first, 'last': emp.last, 'amount': emp.amount})


def get_emp_by_name(lastname):
    cursor.execute("SELECT * FROM employees WHERE last=:last", {'last':lastname})
    return cursor.fetchall()

def update_pay(emp, amount):
    with connection:
        cursor.execute("""UPDATE employees SET amount = :amount
                       WHERE first = :first AND last = :last""",
                       {'first': emp.first, 'last': emp.last, 'amount': amount})

def remove_emp(emp):
    with connection:
        cursor.execute("DELETE FROM employees WHERE first = :first AND last = :last",
                       {'first': emp.first, 'last': emp.last})

# cursor.execute("INSERT INTO employees VALUES ('Khushboo', 'Lo', 50000)")

# cursor.execute("SELECT * FROM employees WHERE last='Lo'")

emp1 = Employee('Pooja' , 'Lo', 85000)
emp2 = Employee('Payal' , 'Kava', 55000)

insert_emp(emp1)
insert_emp(emp2)

emps = get_emp_by_name('Lo')
print(emps)

update_pay(emp2,95000)
remove_emp(emp1)

connection.close()