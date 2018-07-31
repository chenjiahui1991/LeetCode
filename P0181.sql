select a.Name Employee from employee a join employee b on a.ManagerId = b.Id where a.Salary > b.Salary
