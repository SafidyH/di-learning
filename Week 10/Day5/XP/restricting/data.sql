SELECT first_name, last_name, salary
FROM employee
WHERE salary BETWEEN 10000 AND 15000;

SELECT first_name, last_name, hire_date
FROM employee
WHERE EXTRACT(year FROM hire_date) = 1987;

SELECT *
FROM employee
WHERE first_name LIKE '%c%' AND first_name LIKE '%e%';

SELECT last_name, job, salary
FROM employee
WHERE job NOT IN ('Programmer', 'Shipping Clerk') AND salary NOT IN (4500, 10000, 15000);

SELECT last_name
FROM employee
WHERE LENGTH(last_name) = 6;

SELECT last_name
FROM employee
WHERE SUBSTRING(last_name, 3, 1) = 'e';

SELECT DISTINCT job
FROM employee;

SELECT *
FROM employee
WHERE last_name IN ('JONES', 'BLAKE', 'SCOTT', 'KING', 'FORD');
