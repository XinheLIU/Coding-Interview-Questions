# SQL: Window Functions & Ranking

Ranking-within-group problems are where window functions earn their keep. The
pattern: partition the rows into groups, rank inside each group, then filter by
rank in an outer query. The code block below is the actual `.sql` file — edit it
and this page follows.

## Department Top Three Salaries ([#185](https://leetcode.com/problems/department-top-three-salaries/))

**Goal.** For each department, return every employee whose salary is among the top
**three distinct** salaries of that department (ties share a rank).

**Why `DENSE_RANK`, not `ROW_NUMBER`.** Two employees on the same salary must get
the *same* rank, and that salary must not consume two of the three slots.
`DENSE_RANK` gives `1,1,2,3…` (no gaps) — exactly "top three *unique* salaries".
`ROW_NUMBER` would break ties arbitrarily; `RANK` would leave gaps after ties.

**Shape.** `PARTITION BY department` resets the ranking per department;
`ORDER BY salary DESC` puts the highest earners at rank 1; the outer `WHERE rk < 4`
keeps ranks 1–3.

<<< @/problems/185-department-top-three-salaries/solution.sql{sql}
