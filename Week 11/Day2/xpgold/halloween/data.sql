SELECT store_id, city, country
FROM store;

SELECT store_id, SUM(length) AS total_viewing_time_minutes
FROM inventory
WHERE return_date IS NOT NULL
GROUP BY store_id;

SELECT c.customer_id, c.first_name, c.last_name, c.email, s.city, s.country
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city s ON a.city_id = s.city_id
JOIN store st ON s.city_id = st.city_id;

SELECT c.customer_id, c.first_name, c.last_name, c.email, co.country
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city s ON a.city_id = s.city_id
JOIN country co ON s.country_id = co.country_id
JOIN store st ON s.city_id = st.city_id;

SELECT SUM(length) AS total_safe_viewing_time_minutes
FROM film
WHERE category_id <> (SELECT category_id FROM category WHERE name = 'Horror')
AND (title NOT ILIKE '%beast%'
     AND title NOT ILIKE '%monster%'
     AND title NOT ILIKE '%ghost%'
     AND title NOT ILIKE '%dead%'
     AND title NOT ILIKE '%zombie%'
     AND title NOT ILIKE '%undead%'
     AND description NOT ILIKE '%beast%'
     AND description NOT ILIKE '%monster%'
     AND description NOT ILIKE '%ghost%'
     AND description NOT ILIKE '%dead%'
     AND description NOT ILIKE '%zombie%'
     AND description NOT ILIKE '%undead%');

-- For total viewing time in hours
SELECT store_id, SUM(length) / 60 AS total_viewing_time_hours
FROM inventory
WHERE return_date IS NOT NULL
GROUP BY store_id;

-- For total viewing time in days
SELECT store_id, SUM(length) / (60 * 24) AS total_viewing_time_days
FROM inventory
WHERE return_date IS NOT NULL
GROUP BY store_id;

-- For total safe viewing time in hours
SELECT SUM(length) / 60 AS total_safe_viewing_time_hours
FROM film
WHERE category_id <> (SELECT category_id FROM category WHERE name = 'Horror')
AND (title NOT ILIKE '%beast%'
     AND title NOT ILIKE '%monster%'
     AND title NOT ILIKE '%ghost%'
     AND title NOT ILIKE '%dead%'
     AND title NOT ILIKE '%zombie%'
     AND title NOT ILIKE '%undead%'
     AND description NOT ILIKE '%beast%'
     AND description NOT ILIKE '%monster%'
     AND description NOT ILIKE '%ghost%'
     AND description NOT ILIKE '%dead%'
     AND description NOT ILIKE '%zombie%'
     AND description NOT ILIKE '%undead%');

-- For total safe viewing time in days
SELECT SUM(length) / (60 * 24) AS total_safe_viewing_time_days
FROM film
WHERE category_id <> (SELECT category_id FROM category WHERE name = 'Horror')
AND (title NOT ILIKE '%beast%'
     AND title NOT ILIKE '%monster%'
     AND title NOT ILIKE '%ghost%'
     AND title NOT ILIKE '%dead%'
     AND title NOT ILIKE '%zombie%'
     AND title NOT ILIKE '%undead%'
     AND description NOT ILIKE '%beast%'
     AND description NOT ILIKE '%monster%'
     AND description NOT ILIKE '%ghost%'
     AND description NOT ILIKE '%dead%'
     AND description NOT ILIKE '%zombie%'
     AND description NOT ILIKE '%undead%');
