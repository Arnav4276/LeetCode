# Write your MySQL query statement below
select customers.name as "Customers" from Customers left join Orders on Customers.id=Orders.id where Customers.id not in (select customerId from orders);