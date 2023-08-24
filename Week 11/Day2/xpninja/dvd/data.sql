SELECT film_id, title, rating
FROM film
WHERE rating IN ('G', 'PG')
AND film_id NOT IN (SELECT film_id FROM inventory WHERE rental_date IS NOT NULL);

CREATE TABLE children_waiting_list (
    waiting_id SERIAL PRIMARY KEY,
    film_id INTEGER REFERENCES film(film_id),
    child_name VARCHAR(100),
    contact_email VARCHAR(100),
    date_added DATE
);

SELECT film.title, COUNT(*) AS num_waiting
FROM film
JOIN children_waiting_list ON film.film_id = children_waiting_list.film_id
GROUP BY film.title;
