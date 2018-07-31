select Name Customers from (select Name, Orders.Id id from Customers left join Orders on Customers.Id = Orders.CustomerId) as first where first.id is NULL
