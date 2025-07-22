-- Last updated: 22/07/2025, 16:42:11
# Write your MySQL query statement below
select name 
from Customer
where Customer.referee_id is null or Customer.referee_id != 2; 