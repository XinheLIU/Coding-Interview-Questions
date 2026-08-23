-- Question 571
-- The Numbers table keeps the value of number and its frequency.

-- +----------+-------------+
-- |  Number  |  Frequency  |
-- +----------+-------------|
-- |  0       |  7          |
-- |  1       |  1          |
-- |  2       |  3          |
-- |  3       |  1          |
-- +----------+-------------+
-- In this table, the numbers are 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3, so the median is (0 + 0) / 2 = 0.

-- +--------+
-- | median |
-- +--------|
-- | 0.0000 |
-- +--------+
-- Write a query to find the median of all numbers and name the result as median.

-- Solution
/*The idea is that the natural index of the median should be within the range of frequency intervals of each value. 
Also as the intervals are inclusive [start, end] and neighboring intervals share borders, 
the avg() function will help return the median as the mean of two different numbers.

key : find the range [SumFreq / 2, SumFreq / 2 + Frequency] 
*/

with t1 as(
    select 
    *
    , sum(frequency) over(order by num) as acc_freq
    , (sum(frequency) over()) / 2 as middle
    from numbers
)

select avg(num) as median
from t1
where middle between (acc_freq - frequency) and acc_freq