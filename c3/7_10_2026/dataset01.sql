CREATE DATABASE PRODUCT;
use product;
SELECT * FROM superstore;
rename table superstore to store;
select * from store;
select * from store where Segment = "Corporate";
# select Category, SUM(total_sales) as sales from product group by category;
select count(