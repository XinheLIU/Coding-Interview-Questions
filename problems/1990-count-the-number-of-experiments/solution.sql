WITH all_platform (platform) AS (
    SELECT 'Android' AS 'Android' FROM  Experiments
    UNION
    SELECT 'IOS' AS 'IOS' FROM  Experiments 
    UNION 
    SELECT 'Web' AS 'Web' FROM Experiments
),

all_experiment (experiment_name) AS (
    SELECT  'Reading' AS 'Reading' FROM Experiments
    UNION
    SELECT 'Programming' AS 'Programming' FROM Experiments
    UNION
    SELECT'Sports' AS 'Sports' FROM Experiments
)

SELECT
    A.platform,
    A.experiment_name,
    IFNULL(num_experiments,0) AS num_experiments
FROM
(SELECT 
    platform, experiment_name
FROM all_platform CROSS JOIN all_experiment) A
LEFT JOIN 
(SELECT
    platform, experiment_name, COUNT(*) num_experiments
FROM Experiments GROUP BY platform, experiment_name) B
ON A.platform = B.platform AND A.experiment_name = B.experiment_name
ORDER BY A.platform, A.experiment_name


/*
Table: Experiments

+-----------------+------+
| Column Name     | Type |
+-----------------+------+
| experiment_id   | int  |
| platform        | enum |
| experiment_name | enum |
+-----------------+------+
experiment_id is the primary key for this table.
platform is an enum with one of the values ('Android', 'IOS', 'Web').
experiment_name is an enum with one of the values ('Reading', 'Sports', 'Programming').
This table contains information about the ID of an experiment done with a random person, the platform used to do the experiment, and the name of the experiment.
 

Write an SQL query to report the number of experiments done on each of the three platforms for each of the three given experiments. Notice that all the pairs of (platform, experiment) should be included in the output including the pairs with zero experiments.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input:
Experiments table:
+---------------+----------+-----------------+
| experiment_id | platform | experiment_name |
+---------------+----------+-----------------+
| 4             | IOS      | Programming     |
| 13            | IOS      | Sports          |
| 14            | Android  | Reading         |
| 8             | Web      | Reading         |
| 12            | Web      | Reading         |
| 18            | Web      | Programming     |
+---------------+----------+-----------------+
Output: 
+----------+-----------------+-----------------+
| platform | experiment_name | num_experiments |
+----------+-----------------+-----------------+
| Android  | Reading         | 1               |
| Android  | Sports          | 0               |
| Android  | Programming     | 0               |
| IOS      | Reading         | 0               |
| IOS      | Sports          | 1               |
| IOS      | Programming     | 1               |
| Web      | Reading         | 2               |
| Web      | Sports          | 0               |
| Web      | Programming     | 1               |
+----------+-----------------+-----------------+
Explanation: 
On the platform "Android", we had only one "Reading" experiment.
On the platform "IOS", we had one "Sports" experiment and one "Programming" experiment.
On the platform "Web", we had two "Reading" experiments and one "Programming" experiment.
*/