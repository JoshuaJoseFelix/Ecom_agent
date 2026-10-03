
select e.name as employee from Employee e
inner join Employee m where e.managerId=m.id and m.salary<e.salary