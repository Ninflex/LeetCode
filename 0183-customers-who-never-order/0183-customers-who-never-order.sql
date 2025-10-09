# Write your MySQL query statement below
Select name as Customers
FROM Customers
Left Join Orders on Customers.id = Orders.customerId
WHERE Orders.customerId is NULL;