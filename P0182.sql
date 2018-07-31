select Email from (select Email, count(*) amt from Person group by Email) as first where first.amt > 1
