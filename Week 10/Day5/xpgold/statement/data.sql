UPDATE employee
SET email = 'not available', commission_pct = 0.10
WHERE department_id = 110;

UPDATE employee
SET email = 'available'
WHERE department_id IN (SELECT department_id FROM department WHERE department_name = 'Accounting');

UPDATE employee
SET salary = 8000
WHERE employee_id = 105 AND salary < 5000;
