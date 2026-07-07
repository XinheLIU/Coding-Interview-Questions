# Write your MySQL query statement below
SELECT
    d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary
FROM
    Employee e1
        JOIN
    Department d ON e1.DepartmentID = d.ID
WHERE
     (e1.DepartmentId , Salary) IN
        (   SELECT
                DepartmentId, MAX(Salary)
            FROM
                Employee
            GROUP BY DepartmentId
        )
    ;
/*
SELECT 
d.Name "Department",
a.Name "Employee",
a.Salary "Salary"
FROM(
SELECT
    RANK() OVER(PARTITION BY DepartmentId ORDER BY Salary DESC) AS rank,
    Salary,
    Name,
    DepartmentId
    FROM Employee
) a
JOIN Department d
    ON a.DepartmentId = d.Id
WHERE a.rank = 1
ORDER BY "Salary";
*/