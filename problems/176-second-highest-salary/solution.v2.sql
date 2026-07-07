SELECT max(DISTINCT Salary) as SecondHighestSalary from Employee where Salary <  (
    SELECT max(Salary) FROM Employee
)

/*
# Write your MySQL query statement below
# SELECT MAX(Salary) AS SecondHighestSalary FROM Employee WHERE Salary < (SELECT MAX(Salary) FROM Employee)
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;
*/