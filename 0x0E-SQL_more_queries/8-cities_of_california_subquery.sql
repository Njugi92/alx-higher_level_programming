-- This lists all the cities of Califonia in the database hbtn_0d_usa
-- The states table contains only one record where name = California
-- Then results must be sorted in ascending order by cities.id
-- database name will be passed as an argument of the mysql command
SELECT id, name FROM cities
WHERE state_id = (
	SELECT id FROM states
	WHERE name = "Califonia")
ORDER BY id;
