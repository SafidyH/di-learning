SELECT first_name, last_name, salary
FROM employees
WHERE salary > (SELECT salary FROM employees WHERE last_name = 'Bull');

SELECT first_name, last_name
FROM employees
WHERE manager_id IN (
    SELECT employee_id
    FROM employees
    WHERE department_id IN (
        SELECT department_id
        FROM departments
        WHERE location_id IN (
            SELECT location_id
            FROM locations
            WHERE country_id IN (
                SELECT country_id
                FROM countries
                WHERE country_name = 'United States'
            )
        )
    )
);

SELECT first_name, last_name
FROM employees
WHERE employee_id IN (
    SELECT manager_id
    FROM employees
);

SELECT first_name, last_name
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

SELECT first_name, last_name
FROM employees
WHERE salary = (SELECT MIN(salary) FROM employees e2 WHERE employees.job_id = e2.job_id);

SELECT first_name, last_name
FROM employees
WHERE employee_id NOT IN (SELECT DISTINCT manager_id FROM employees WHERE manager_id IS NOT NULL);

SELECT employee_id, first_name, last_name, salary
FROM employees e1
WHERE salary > (SELECT AVG(salary) FROM employees e2 WHERE e1.department_id = e2.department_id);

SELECT DISTINCT salary
FROM employees e1
WHERE 5 = (SELECT COUNT(DISTINCT salary) FROM employees e2 WHERE e2.salary >= e1.salary);

SELECT DISTINCT salary
FROM employees e1
WHERE 4 = (SELECT COUNT(DISTINCT salary) FROM employees e2 WHERE e2.salary <= e1.salary);

SELECT department_name, department_id
FROM departments
WHERE department_id NOT IN (SELECT department_id FROM employees);


SELECT d.location_id, l.street_address, l.city, l.state_province, c.country_name
FROM departments d
JOIN locations l ON d.location_id = l.location_id
JOIN countries c ON l.country_id = c.country_id;

SELECT e.first_name, e.last_name, d.department_id, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

SELECT e.first_name, e.last_name, j.job_title, d.department_name, d.department_id
FROM employees e
JOIN jobs j ON e.job_id = j.job_id
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
WHERE l.city = 'London';

SELECT e1.employee_id AS EmployeeID, e1.last_name AS Employee, e1.manager_id, e2.last_name AS Manager
FROM employees e1
JOIN employees e2 ON e1.manager_id = e2.employee_id;

SELECT e.first_name, e.last_name, e.employee_id, d.department_name, d.department_id
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

SELECT e.employee_id, j.job_title, COUNT(r.rental_date) AS NumberOfWorkingDays
FROM employees e
JOIN jobs j ON e.job_id = j.job_id
JOIN rentals r ON e.employee_id = r.employee_id
JOIN departments d ON e.department_id = d.department_id
WHERE d.department_id = 90
GROUP BY e.employee_id, j.job_title;

SELECT d.department_name, CONCAT(e.first_name, ' ', e.last_name) AS ManagerName, l.city
FROM departments d
JOIN employees e ON d.manager_id = e.employee_id
JOIN locations l ON d.location_id = l.location_id;

SELECT j.job_title, AVG(e.salary) AS AverageSalary
FROM employees e
JOIN jobs j ON e.job_id = j.job_id
GROUP BY j.job_title;

SELECT d.department_name, e.first_name, e.last_name, e.hire_date, e.salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.employee_id = d.manager_id AND EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM e.hire_date) > 15;



UPDATE employees
SET phone_number = '999'
WHERE phone_number LIKE '%124%';

SELECT *
FROM employees
WHERE LENGTH(first_name) >= 8;

SELECT CONCAT(UPPER(SUBSTRING(first_name, 1, 1)), last_name, '@example.com') AS EMAIL
FROM employees;

SELECT employee_id, SUBSTRING(email, 1, LENGTH(email) - 3) AS email
FROM employees;

SELECT 
  CASE 
    WHEN POSITION(' ' IN job_title) > 0 THEN SUBSTRING(job_title, 1, POSITION(' ' IN job_title) - 1)
    ELSE job_title
  END AS first_word_in_job_title
FROM employees;

SELECT 
  first_name, 
  LENGTH(first_name) AS length_of_first_name
FROM employees
WHERE first_name LIKE 'A%' OR first_name LIKE 'J%' OR first_name LIKE 'M%'
ORDER BY first_name;

SELECT 
  first_name, 
  CONCAT('$', salary) AS SALARY
FROM employees;
