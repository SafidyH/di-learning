SELECT rating, COUNT(*) AS film_count
FROM film
GROUP BY rating;

SELECT film_id, title, rating, length, rental_rate
FROM film
WHERE rating IN ('G', 'PG-13') AND length <= 120 AND rental_rate < 3.00
ORDER BY title;

UPDATE customer
SET first_name = 'John', last_name = 'Doe'
WHERE customer_id = 1;

UPDATE address
SET address = '123 Main Street'
WHERE address_id = (
    SELECT address_id
    FROM customer
    WHERE customer_id = 1
);
