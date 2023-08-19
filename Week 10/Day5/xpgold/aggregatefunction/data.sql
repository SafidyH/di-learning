SELECT COUNT(DISTINCT job) AS number_of_jobs
FROM employees;


SELECT job, COUNT(*) AS number_of_employees
FROM employees
GROUP BY job;

SELECT MAX(salary) - MIN(salary) AS salary_difference
FROM employees;

SELECT manager_id, MIN(salary) AS lowest_salary
FROM employees
GROUP BY manager_id;

SELECT job, AVG(salary) AS average_salary
FROM employees
WHERE job != 'Programmer'
GROUP BY job;

SELECT department_id, AVG(salary) AS average_salary
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 10;
