
SELECT * FROM customer;
SELECT first_name || ' ' || last_name AS full_name FROM customer;
SELECT DISTINCT create_date FROM customer;
SELECT * FROM customer ORDER BY first_name DESC;
SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate;
SELECT a.address, a.phone FROM address a
JOIN city c ON a.city_id = c.city_id
JOIN country co ON c.country_id = co.country_id
WHERE co.country = 'United States' AND c.city = 'Texas';
SELECT * FROM film WHERE film_id IN (15, 150);
SELECT film_id, title, description, length, rental_rate FROM film WHERE title = 'Your Favorite Movie';
SELECT film_id, title, description, length, rental_rate FROM film WHERE title LIKE 'Your_Favorite_Letters%';
SELECT * FROM film ORDER BY rental_rate LIMIT 10;
SELECT * FROM film WHERE film_id NOT IN (SELECT film_id FROM film ORDER BY rental_rate LIMIT 10) ORDER BY rental_rate LIMIT 10;
SELECT c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY c.customer_id;
SELECT * FROM film f
WHERE NOT EXISTS (
    SELECT 1 FROM inventory i WHERE f.film_id = i.film_id
);
SELECT c.city, co.country
FROM city c
JOIN country co ON c.country_id = co.country_id;
SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, s.staff_id
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
JOIN rental r ON p.rental_id = r.rental_id
JOIN staff s ON r.staff_id = s.staff_id
ORDER BY s.staff_id;
