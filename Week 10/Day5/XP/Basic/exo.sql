SELECT first_name AS First, last_name AS Last
FROM employees;

SELECT DISTINCT department_id
FROM employees;

SELECT first_name AS "First", last_name AS "Last"
FROM employee;


SELECT DISTINCT department_id
FROM employee;


SELECT *
FROM employee
ORDER BY first_name DESC;

SELECT first_name, last_name, salary, salary * 0.15 AS PF
FROM employee;

SELECT employee_id, first_name, last_name, salary
FROM employee
ORDER BY salary ASC;


SELECT SUM(salary) AS total_salary
FROM employee;


SELECT MAX(salary) AS max_salary, MIN(salary) AS min_salary
FROM employee;


SELECT AVG(salary) AS average_salary
FROM employee;


SELECT COUNT(*) AS num_employees
FROM employee;


SELECT UPPER(first_name) AS first_name_upper
FROM employee;

SELECT SUBSTRING(first_name, 1, 3) AS first_name_chars
FROM employee;


SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM employee;

SELECT first_name, last_name, LENGTH(first_name || ' ' || last_name) AS full_name_length
FROM employee;


SELECT *
FROM employee
WHERE first_name ~ '[0-9]';

SELECT *
FROM employee
LIMIT 10;

