select distinct f.title,f.rating
from film f
join film_category fc on f.film_id = fc.film_id
where fc.category_id = 5 and f.rating='PG-13';

select distinct f.title,f.rental_rate
from film f
join film_category fc on f.film_id = fc.film_id
where fc.category_id = 11
order by f.rental_rate desc
limit 3;

SELECT c.first_name,c.customer_id
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ct ON a.city_id = ct.city_id
JOIN (
  SELECT DISTINCT customer_id
  FROM rental r
  JOIN inventory i ON r.inventory_id = i.inventory_id
  JOIN film f ON i.film_id = f.film_id
  JOIN film_category fc ON f.film_id = fc.film_id
  WHERE fc.category_id = 15
) AS film_customers ON c.customer_id = film_customers.customer_id
WHERE ct.country_id = 44;

SELECT DISTINCT c.customer_id, c.first_name
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ct ON a.city_id = ct.city_id
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film_actor fa ON i.film_id = fa.film_id
WHERE ct.country_id = 20 AND fa.actor_id = 2;

select count(film_id) from film_actor where actor_id = 72;


