# Write your MySQL query statement below
select * from Cinema 
where MOD(id,2) = 1 
and LOWER(description) NOT LIKE 'boring'
ORDER BY rating DESC;