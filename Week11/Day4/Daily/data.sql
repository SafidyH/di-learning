CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL
);

CREATE TABLE product_orders (
    order_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    order_date DATE NOT NULL
);

ALTER TABLE items ADD COLUMN order_id INTEGER REFERENCES product_orders(order_id);

CREATE OR REPLACE FUNCTION calculate_total_price(order_id INTEGER)
RETURNS NUMERIC AS $$
DECLARE
    total_price NUMERIC := 0;
BEGIN
    SELECT SUM(price) INTO total_price
    FROM items
    WHERE order_id = calculate_total_price.order_id;
    
    RETURN total_price;
END;
$$ LANGUAGE PLPGSQL;

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE OR REPLACE FUNCTION calculate_total_price_for_user(user_id INTEGER, order_id INTEGER)
RETURNS NUMERIC AS $$
DECLARE
    total_price NUMERIC := 0;
BEGIN
    SELECT SUM(price) INTO total_price
    FROM items
    WHERE order_id = calculate_total_price_for_user.order_id
    AND EXISTS (
        SELECT 1 FROM product_orders
        WHERE order_id = calculate_total_price_for_user.order_id
        AND user_id = calculate_total_price_for_user.user_id
    );
    
    RETURN total_price;
END;
$$ LANGUAGE PLPGSQL;
