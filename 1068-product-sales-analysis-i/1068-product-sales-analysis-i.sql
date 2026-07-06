# Write your MySQL query statement below
select Product.product_name, s.year, s.price
from Sales s
Join Product
On s.product_id=Product.product_id;