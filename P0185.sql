select x.Department
    , x.Employee
    , x.Salary
from
(
    select d.Name as Department
      , e.Name as Employee
      , e.Salary
      , (select count(distinct salary)
         from Employee as r
         where r.salary > e.salary
           and r.DepartmentId = e.DepartmentId) as rank
    from Employee as e
    join Department as d
      on e.DepartmentId = d.Id
) as x
where x.rank < 3
order by x.Department, x.Salary desc
