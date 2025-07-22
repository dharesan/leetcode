-- Last updated: 22/07/2025, 16:42:24
SELECT E.name AS Employee
FROM Employee E
JOIN Employee M ON E.managerId = M.id
WHERE E.salary > M.salary;
