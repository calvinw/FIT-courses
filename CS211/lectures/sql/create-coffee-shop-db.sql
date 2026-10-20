CREATE TABLE products (
  product_id int NOT NULL,
  name varchar(255),
  category varchar(255),
  price decimal(10,2),
  in_stock tinyint,
  PRIMARY KEY (product_id)
);

INSERT INTO products (product_id, name, category, price, in_stock) VALUES
(1, 'Espresso', 'Coffee', 2.50, 1),
(2, 'Cappuccino', 'Coffee', 3.50, 1),
(3, 'Latte', 'Coffee', 3.75, 1),
(4, 'Americano', 'Coffee', 2.75, 1),
(5, 'Matcha Latte', 'Tea', 4.25, 1),
(6, 'Earl Grey', 'Tea', 2.50, 1),
(7, 'Chocolate Croissant', 'Pastry', 3.25, 1),
(8, 'Blueberry Muffin', 'Pastry', 2.95, 1),
(9, 'Iced Coffee', 'Coffee', 3.25, 1),
(10, 'Chai Latte', 'Tea', 3.95, 1),
(11, 'Lemon Tart', 'Pastry', 4.50, 1),
(12, 'Cold Brew', 'Coffee', 4.00, 1);

CREATE TABLE orders (
  order_id int NOT NULL,
  product_id int NOT NULL,
  customer_name varchar(255),
  quantity int,
  order_date date,
  completed tinyint,
  PRIMARY KEY (order_id),
  FOREIGN KEY (product_id) REFERENCES products (product_id)
);

INSERT INTO orders (order_id, product_id, customer_name, quantity, order_date, completed) VALUES
(1, 2, 'John Smith', 1, '2025-04-13', 1),
(2, 7, 'John Smith', 1, '2025-04-13', 1),
(3, 5, 'Emma Johnson', 1, '2025-04-13', 1),
(4, 10, 'Michael Brown', 2, '2025-04-13', 1),
(5, 1, 'Sarah Davis', 1, '2025-04-13', 1),
(6, 3, 'David Wilson', 1, '2025-04-13', 0),
(7, 8, 'David Wilson', 2, '2025-04-13', 0),
(8, 9, 'Jennifer Lee', 1, '2025-04-13', 0),
(9, 4, 'Robert Taylor', 1, '2025-04-13', 0),
(10, 6, 'Lisa Anderson', 3, '2025-04-13', 0);
