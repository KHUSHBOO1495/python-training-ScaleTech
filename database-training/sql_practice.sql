CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES (1, 'Khushboo', 'IT', 50000);

INSERT INTO employees (id, name, department, salary)
VALUES (2, 'Payal', 'HR', 45000);

SELECT * FROM employees;

SELECT name, salary
FROM employees;

SELECT *
FROM employees
WHERE department = 'IT';

SELECT *
FROM employees
WHERE salary > 48000;

SELECT *
FROM employees
WHERE department = 'IT'
AND salary > 48000;

SELECT *
FROM employees
WHERE department = 'IT'
OR department = 'HR';

SELECT *
FROM employees
ORDER BY salary DESC;

SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 1;