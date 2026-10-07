Tools used: MySQL Workbench 

database : dataset01
Scheme : product
Table : store

code used:

	CREATE DATABASE PRODUCT;
	use product;
	SELECT * FROM superstore;
	rename table superstore to store;
	select * from store;
	select * from store where Segment = "Corporate";
	# select Category, SUM(total_sales) as sales from product group by category;
	select count(*) as total_row_count from store;
	select distinct Region as cust_country from store;
