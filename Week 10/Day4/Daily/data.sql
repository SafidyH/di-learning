SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id IS NULL);

SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id = 5);

SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN (SELECT id FROM SecondTab);

SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id IS;

-- Query 1
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id IS NULL);

--Explanation: The subquery (SELECT id FROM SecondTab WHERE id IS NULL) will return a single row with a NULL value. So, the main query will return the count of rows in FirstTab where the id is not NULL, which is 3.

-- Query 2
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id = 5);

--Explanation: The subquery (SELECT id FROM SecondTab WHERE id = 5) will return a single row with the value 5. So, the main query will return the count of rows in FirstTab where the id is not equal to 5, which is 2.

-- Query 3
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN (SELECT id FROM SecondTab);

--Explanation: The subquery (SELECT id FROM SecondTab) will return two rows (5 and NULL). So, the main query will return the count of rows in FirstTab where the id is not equal to any of the values returned by the subquery, which is 1 (ID = 7).

-- Query 4
-- There is a syntax error in this query.
--Explanation: The subquery (SELECT id FROM SecondTab WHERE id IS) is invalid as it does not have a condition after IS. The query will result in a syntax error and will not execute.
