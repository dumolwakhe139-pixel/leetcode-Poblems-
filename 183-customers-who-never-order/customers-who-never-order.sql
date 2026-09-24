/* Write your PL/SQL query statement below */
SELECT C.NAME AS CUSTOMERS FROM 
customers C LEFT  JOIN ORDERS  O
ON C.id  = O.CUSTOMERID
WHERE O.ID IS NULL ;
