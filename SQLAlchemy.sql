
SELECT * FROM orm_customers;


SELECT * FROM orm_orders;


SELECT
    c.name,
    COUNT(o.id) AS order_count
FROM orm_customers c
LEFT JOIN orm_orders o
    ON c.id = o.customer_id
GROUP BY c.id, c.name
ORDER BY c.id;
