CREATE TABLE new_countries (
    country_id INT PRIMARY KEY,
    country_name VARCHAR(50) UNIQUE,
    CHECK (country_name IN ('Italy', 'India', 'China'))
);

CREATE TABLE new_countries_copy AS
SELECT * FROM new_countries;

CREATE TABLE new_jobs (
    job_id INT PRIMARY KEY,
    job_title VARCHAR(50) DEFAULT '',
    min_salary DECIMAL(10,2) DEFAULT 8000,
    max_salary DECIMAL(10,2) DEFAULT NULL CHECK (max_salary <= 25000)
);

CREATE TABLE new_employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone_number VARCHAR(20),
    hire_date DATE,
    job_id INT,
    salary DECIMAL(10,2),
    UNIQUE (employee_id),
    FOREIGN KEY (job_id) REFERENCES new_jobs (job_id)
);

CREATE TABLE new_job_history (
    employee_id INT,
    start_date DATE,
    end_date DATE,
    job_id INT,
    FOREIGN KEY (employee_id) REFERENCES new_employees (employee_id),
    FOREIGN KEY (job_id) REFERENCES new_jobs (job_id)
);

INSERT INTO new_countries (country_id, country_name) VALUES (1, 'United States');

INSERT INTO new_countries (country_id, country_name)
VALUES (2, 'United Kingdom'), (3, 'Canada'), (4, 'Australia');

CREATE TABLE new_countries_duplicate AS
SELECT * FROM new_countries;

INSERT INTO new_employees (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary)
VALUES (1, 'John', 'Doe', 'john.doe@example.com', '1234567890', '2023-08-01', 1, 50000),
       (2, 'Jane', 'Smith', 'jane.smith@example.com', '9876543210', '2023-08-02', 2, 60000);
