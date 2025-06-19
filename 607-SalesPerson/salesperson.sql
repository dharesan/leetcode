# Write your MySQL query statement belowse

-- with no_RED_com_id as (
--     select com_id from Company where name != 'RED'
-- ),

-- temp_table as (
--     select SalesPerson.name, SalesPerson.sales_id from SalesPerson left join Orders on SalesPerson.sales_id = Orders.sales_id 
-- ) 

-- select name from temp_table where Orders.com_id 

-- left join on com_id Orders <--> Company 

-- with tempTable as (
--     select com_id from Company where name
-- )

-- select SalesPerson.name as salespersonName, Company.name as companyName
-- from SalesPerson 
-- left join SalesPerson on Orders.sales_id = SalesPerson.sales_id
-- left join Orders on Orders.com_id = Company.com_id 
-- where Company.name != "RED"


-- query who sold to company "RED" first 

select name from SalesPerson where sales_id not in (

select Orders.sales_id
from Orders 
left join Company on Orders.com_id = Company.com_id
where Company.name = "RED"
);
