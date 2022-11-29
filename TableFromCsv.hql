
create database if not exists test_db
;

use test_db;

drop table if exists WWI_Sales_Orders
;

create table if not exists WWI_Sales_Orders
(
	OrderID int,
	CustomerID int,
	SalespersonPersonID int,
	PickedByPersonID int,
	ContactPersonID int,
	BackorderOrderID int,
	ExpectedDeliveryDate date,
	CustomerPurchaseOrderNumber varchar(20),
	IsUndersupplyBackordered TINYINT,
	Comments varchar(65535),
	DeliveryInstructions varchar(65535),
	InternalComments varchar(65535),
	PickingCompletedWhen timestamp,
	LastEditedBy int,
	LastEditedWhen timestamp,
	OrderDate date
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
TBLPROPERTIES ("skip.header.line.count"="1")
;

LOAD DATA LOCAL INPATH '/mnt/WWI_Sales_Orders.csv' INTO TABLE WWI_Sales_Orders
;

select * from WWI_Sales_Orders limit 100
;
