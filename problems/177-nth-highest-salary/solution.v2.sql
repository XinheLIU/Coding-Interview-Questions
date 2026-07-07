CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT e1.Salary FROM employee e1 WHERE N-1 = (
        SELECT COUNT(DISTINCT e2.Salary) 
          FROM employee e2
          WHERE e1.Salary < e2.Salary
      )
  );
END

/*
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N - 1;
RETURN (

  # Write your MySQL query statement below.
  SELECT IFNULL(
  (SELECT distinct salary
  from  Employee
  ORDER BY Salary desc
  limit 1 offset N)
      ,NULL)
);
END

*/