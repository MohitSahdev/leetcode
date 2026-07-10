# Write your MySQL query statement below
select visits.customer_id, count(*) as count_no_trans
from Visits
left join Transactions t
on visits.visit_id=t.visit_id
where t.transaction_id IS NULL
Group by visits.customer_id