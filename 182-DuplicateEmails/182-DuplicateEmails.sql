-- Last updated: 22/07/2025, 16:42:21
# Write your MySQL query statement below
-- SELECT COUNT(id), email 
-- FROM Person 
-- GROUP BY email 

SELECT email
FROM Person 
GROUP BY email 
HAVING COUNT(email) > 1





