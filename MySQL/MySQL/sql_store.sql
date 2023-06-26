DROP DATABASE IF EXISTS sql_store;
CREATE DATABASE sql_store;
USE sql_store;

CREATE TABLE products(
	product_id        INT PRIMARY KEY AUTO_INCREMENT,
    name              VARCHAR(50) NOT NULL,
    unit_price        DECIMAL(5, 2) NOT NULL,
    quantity_in_stock INT
    
);

INSERT INTO products(name, unit_price, quantity_in_stock) VALUES('Pencil', 0.10, 400);
INSERT INTO products(name, unit_price, quantity_in_stock) VALUES('Pen', 0.15, 200);
INSERT INTO products(name, unit_price, quantity_in_stock) VALUES('Paper', 0.10, 2000);
INSERT INTO products(name, unit_price, quantity_in_stock) VALUES('Scissor', 1.50, 60);
INSERT INTO products(name, unit_price, quantity_in_stock) VALUES('Marker', 0.30, 200);
INSERT INTO products(name, unit_price, quantity_in_stock) VALUES('Eraser', 0.99, 100);
INSERT INTO products(name, unit_price, quantity_in_stock) VALUES('Notebook', 0.30, 100);
INSERT INTO products(name, unit_price, quantity_in_stock) VALUES('Pencil Box', 1.99, 80);
INSERT INTO products(name, unit_price, quantity_in_stock) VALUES('Backpack', 10.00, 40);
INSERT INTO products(name, unit_price, quantity_in_stock) VALUES('Geometry Kit', 2.99, 80);


CREATE TABLE customers(
	customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    email VARCHAR(40) NOT NULL UNIQUE,
    state VARCHAR(2) NOT NULL
);

CREATE TABLE cust_passwd(
	customer_id INT PRIMARY KEY,
    password VARCHAR(20) UNIQUE,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE orders(
	order_id    INT NOT NULL ,
    customer_id INT NOT NULL ,
    product_id  INT NOT NULL , 
    quantity    INT NOT NULL,
    PRIMARY KEY(order_id, product_id),
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY(product_id) REFERENCES products(product_id) ON DELETE CASCADE
);
