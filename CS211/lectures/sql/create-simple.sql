CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10, 2),
    in_stock INT
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    product_id INT,
    customer VARCHAR(255),
    qty INT,
    completed INT,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

INSERT INTO Products (product_id, name, price, in_stock) VALUES
(1, 'Wireless Headphones', 79.99, 1),
(2, 'Coffee Beans', 14.99, 1),
(3, 'T-Shirt', 24.99, 1),
(4, 'USB-C Cable', 12.99, 0);

INSERT INTO Orders (order_id, product_id, customer, qty, completed) VALUES
(101, 1, 'Alice', 2, 1),
(102, 2, 'Bob', 5, 1),
(103, 3, 'Carol', 3, 0),
(104, 1, 'David', 1, 1),
(105, 3, 'Alice', 1, 1);