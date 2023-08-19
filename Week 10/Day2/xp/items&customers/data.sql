-- Create the public database
CREATE DATABASE public;

-- Switch to the public database
\c public;

-- Create the items table
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price INTEGER NOT NULL
);

-- Insert data into the items table
INSERT INTO items (name, price) VALUES
    ('Small Desk', 100),
    ('Large Desk', 300),
    ('Fan', 80);

-- Create the customers table
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

-- Insert data into the customers table
INSERT INTO customers (first_name, last_name) VALUES
    ('Greg', 'Jones'),
    ('Sandra', 'Jones'),
    ('Scott', 'Scott'),
    ('Trevor', 'Green'),
    ('Melanie', 'Johnson');

-- Fetch all the items
SELECT * FROM items;

-- Fetch all the items with a price above 80 (80 not included)
SELECT * FROM items WHERE price > 80;

-- Fetch all the items with a price below 300 (300 included)
SELECT * FROM items WHERE price <= 300;

-- Fetch all customers whose last name is 'Smith'
SELECT * FROM customers WHERE last_name = 'Smith';

-- Fetch all customers whose last name is 'Jones'
SELECT * FROM customers WHERE last_name = 'Jones';

-- Fetch all customers whose first name is not 'Scott'
SELECT * FROM customers WHERE first_name <> 'Scott';
