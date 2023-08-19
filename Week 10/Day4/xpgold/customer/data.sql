-- Create the purchases table
CREATE TABLE purchases (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    item_id INTEGER REFERENCES items(id),
    quantity_purchased INTEGER
);

-- Insert purchases for the customers
INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES
    (3, 3, 1), -- Scott Scott bought one fan
    (5, 2, 10), -- Melanie Johnson bought ten large desks
    (1, 1, 2); -- Greg Jones bought two small desks

SELECT * FROM purchases;

SELECT purchases.*, customers.first_name, customers.last_name
FROM purchases
JOIN customers ON purchases.customer_id = customers.id;

SELECT * FROM purchases
WHERE customer_id = 5;

SELECT * FROM purchases
WHERE item_id IN (1, 2);

SELECT customers.first_name, customers.last_name, items.item_name
FROM customers
JOIN purchases ON customers.id = purchases.customer_id
JOIN items ON purchases.item_id = items.id;

-- This will not work because the foreign key constraint requires the referenced item_id to exist in the items table.
INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (2, NULL, 3);
