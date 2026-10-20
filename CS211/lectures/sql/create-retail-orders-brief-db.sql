CREATE TABLE customers (
  customer_id int NOT NULL,
  first_name varchar(255),
  last_name varchar(255),
  PRIMARY KEY (customer_id)
);

INSERT INTO customers (customer_id, first_name, last_name) VALUES
(1, 'John', 'Doe'),
(2, 'Jane', 'Smith'),
(3, 'Robert', 'Johnson'),
(4, 'Sarah', 'Williams');

CREATE TABLE products (
  product_id int NOT NULL,
  name varchar(255),
  price decimal(10,2),
  PRIMARY KEY (product_id)
);

INSERT INTO products (product_id, name, price) VALUES
(1, 'Silk Blouse', 89.99),
(2, 'Denim Jeans', 79.99),
(3, 'Cashmere Sweater', 149.99),
(4, 'Cotton T-Shirt', 29.99),
(5, 'Wool Coat', 199.99);

CREATE TABLE orders (
  order_id int NOT NULL,
  customer_id int NOT NULL,
  product_id int NOT NULL,
  order_date date,
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
  FOREIGN KEY (product_id) REFERENCES products (product_id)
);

INSERT INTO orders (order_id, customer_id, product_id, order_date) VALUES
(1, 1, 3, '2025-03-10'),
(2, 2, 1, '2025-03-12'),
(3, 3, 4, '2025-03-15'),
(4, 2, 4, '2025-03-18'),
(5, 1, 2, '2025-03-20'),
(6, 2, 3, '2025-03-25');
