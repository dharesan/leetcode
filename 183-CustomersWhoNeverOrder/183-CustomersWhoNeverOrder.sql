-- Last updated: 22/07/2025, 16:42:20
# Write your MySQL query statement below
select Customers.name as Customers from Customers left join Orders on Customers.id = Orders.customerId where Orders.customerId is null; 