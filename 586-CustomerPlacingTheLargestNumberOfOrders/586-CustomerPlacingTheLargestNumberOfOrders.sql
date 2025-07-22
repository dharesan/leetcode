-- Last updated: 22/07/2025, 16:42:09
# Write your MySQL query statement below
select customer_number from Orders group by customer_number order by count(customer_number) desc
limit 1; 