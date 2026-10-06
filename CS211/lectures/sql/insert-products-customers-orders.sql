INSERT INTO products (name, price, description) VALUES
('Running Shoes', 119.99, 'Lightweight athletic footwear'),
('Yoga Pants', 59.99, 'Stretchy workout leggings'),
('Wool Scarf', 39.99, 'Warm winter accessory'),
('Canvas Sneakers', 69.99, 'Comfortable casual shoes'),
('Rain Jacket', 89.99, 'Waterproof shell'),
('Flannel Shirt', 54.99, 'Cozy plaid button-up'),
('Hiking Boots', 159.99, 'Durable trail footwear'),
('Baseball Cap', 24.99, 'Adjustable sports hat'),
('Leather Belt', 44.99, 'Classic dress accessory'),
('Summer Dress', 79.99, 'Flowy floral pattern');

INSERT INTO customers (first_name, last_name, email) VALUES
('Emily', 'Davis', 'emily.davis@example.com'),
('David', 'Martinez', 'david.martinez@example.com'),
('Jessica', 'Garcia', 'jessica.garcia@example.com'),
('Christopher', 'Wilson', 'christopher.wilson@example.com'),
('Amanda', 'Anderson', 'amanda.anderson@example.com');

INSERT INTO orders (customer_id, product_id, order_date) VALUES
(1, 11, '2024-11-25 10:30:00'),
(2, 12, '2024-11-26 14:15:00'),
(9, 13, '2024-11-27 09:45:00'),
(10, 14, '2024-11-28 16:20:00'),
(11, 15, '2024-11-29 11:00:00');
