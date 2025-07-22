-- Last updated: 22/07/2025, 16:42:12
# Write your MySQL query statement below
select Employee.name, Bonus.bonus from Employee left join Bonus on Employee.empId = Bonus.empId where Bonus.bonus is null or Bonus.bonus < 1000; 