# Write your MySQL query statement below
-- SELECT COUNT(id), email 
-- FROM Person 
-- GROUP BY email 

SELECT email
FROM Person 
GROUP BY email 
HAVING COUNT(email) > 1





