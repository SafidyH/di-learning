SELECT rental_id, rental_date, return_date
FROM rental
WHERE return_date IS NULL;

SELECT customer_id, first_name, last_name, COUNT(*) AS outstanding_rentals
FROM customer
JOIN rental USING (customer_id)
WHERE return_date IS NULL
GROUP BY customer_id, first_name, last_name;

SELECT film.film_id, film.title, film.description, film.rating, film.release_year, film.rental_duration, film.rental_rate, film.length
FROM film
JOIN film_category USING (film_id)
JOIN category USING (category_id)
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE category.name = 'Action' AND actor.first_name = 'Joe' AND actor.last_name = 'Swank';

CREATE VIEW Action_Films_With_Joe_Swank AS
SELECT film.film_id, film.title, film.description, film.rating, film.release_year, film.rental_duration, film.rental_rate, film.length
FROM film
JOIN film_category USING (film_id)
JOIN category USING (category_id)
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE category.name = 'Action' AND actor.first_name = 'Joe' AND actor.last_name = 'Swank';

SELECT * FROM Action_Films_With_Joe_Swank;
