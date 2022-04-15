SELECT address,city_id 
FROM address as a
WHERE substring(a.address,1,2) LIKE '11'
AND a.city_id BETWEEN 400 AND 600;