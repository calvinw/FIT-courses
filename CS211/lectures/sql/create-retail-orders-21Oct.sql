CREATE TABLE customers (
  customer_id int NOT NULL,
  first_name varchar(255),
  last_name varchar(255),
  email varchar(255),
  PRIMARY KEY (customer_id)
);

INSERT INTO customers (customer_id, first_name, last_name, email) VALUES
(1, 'John', 'Doe', 'john.doe@example.com'),
(2, 'Jane', 'Smith', 'jane.smith@example.com'),
(3, 'Robert', 'Johnson', 'robert.johnson@example.com'),
(4, 'Sarah', 'Williams', 'sarah.williams@example.com'),
(5, 'Michael', 'Brown', 'michael.brown@example.com'),
(6, 'Emily', 'Jones', 'emily.jones@example.com'),
(7, 'David', 'Miller', 'david.miller@example.com'),
(8, 'Lisa', 'Davis', 'lisa.davis@example.com');

CREATE TABLE products (
  product_id int NOT NULL,
  name varchar(255),
  price decimal(10,2),
  description varchar(1023),
  PRIMARY KEY (product_id)
);

INSERT INTO products (product_id, name, price, description) VALUES
(1, 'Silk Blouse', 89.99, 'Elegant office wear'),
(2, 'Denim Jeans', 79.99, 'Classic straight cut'),
(3, 'Cashmere Sweater', 149.99, 'Soft winter essential'),
(4, 'Leather Jacket', 249.99, 'Stylish outerwear'),
(5, 'Cotton T-Shirt', 29.99, 'Casual everyday staple'),
(6, 'Linen Dress', 119.99, 'Perfect summer outfit'),
(7, 'Wool Coat', 199.99, 'Warm winter classic'),
(8, 'Canvas Sneakers', 59.99, 'Comfortable streetwear'),
(9, 'Satin Skirt', 69.99, 'Versatile evening piece'),
(10, 'Knit Cardigan', 89.99, 'Cozy layering option');

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
(3, 3, 5, '2025-03-15'),
(4, 2, 5, '2025-03-18'),
(5, 4, 2, '2025-03-20'),
(6, 5, 5, '2025-03-22'),
(7, 2, 3, '2025-03-25'),
(8, 6, 2, '2025-03-28'),
(9, 7, 1, '2025-04-01'),
(10, 1, 3, '2025-04-05');
