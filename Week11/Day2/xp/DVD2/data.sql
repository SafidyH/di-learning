UPDATE film
SET language_id = (SELECT language_id FROM language WHERE name = 'Spanish')
WHERE title IN ('Film A', 'Film B');

DROP TABLE customer_review;

SELECT COUNT(*) AS outstanding_rentals
FROM rental
WHERE return_date IS NULL;

SELECT film_id, title, rental_rate
FROM rental
JOIN inventory USING (inventory_id)
JOIN film USING (film_id)
WHERE return_date IS NULL
ORDER BY rental_rate DESC
LIMIT 30;

SELECT title, description, release_year, actor.first_name, actor.last_name
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE description LIKE '%sumo wrestler%'
  AND (actor.first_name = 'Penelope' AND actor.last_name = 'Monroe');

SELECT title, description, length, rating
FROM film
WHERE length < '01:00:00'
  AND rating = 'R';

SELECT film.title, film.description, rental.rental_date, rental.return_date, payment.amount
FROM film
JOIN inventory USING (film_id)
JOIN rental USING (inventory_id)
JOIN payment USING (rental_id)
JOIN customer ON rental.customer_id = customer.customer_id
WHERE customer.first_name = 'Matthew'
  AND customer.last_name = 'Mahan'
  AND payment.amount > 4.00
  AND rental.rental_date BETWEEN '2005-07-28' AND '2005-08-01';

SELECT film.title, film.description, film.replacement_cost
FROM film
JOIN inventory USING (film_id)
JOIN rental USING (inventory_id)
JOIN customer ON rental.customer_id = customer.customer_id
WHERE customer.first_name = 'Matthew'
  AND customer.last_name = 'Mahan'
  AND (film.title LIKE '%boat%' OR film.description LIKE '%boat%')
  AND film.replacement_cost > 20.00;
