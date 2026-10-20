-- Fashion Boutique database: stores, products, inventory
-- Run the whole script at once. inventory refers to the other two tables, so it is created last.

CREATE TABLE stores (
  store_id int NOT NULL,
  store_name varchar(255),
  city varchar(255),
  opened_date date,
  PRIMARY KEY (store_id)
);

INSERT INTO stores (store_id, store_name, city, opened_date) VALUES
(1, 'SoHo Flagship', 'New York', '2018-03-15'),
(2, 'Williamsburg', 'Brooklyn', '2021-09-01'),
(3, 'Hoboken', 'Hoboken', '2023-05-20');

CREATE TABLE products (
  product_id int NOT NULL,
  name varchar(255),
  category varchar(255),
  color varchar(255),
  cost decimal(10,2),
  price decimal(10,2),
  PRIMARY KEY (product_id)
);

INSERT INTO products (product_id, name, category, color, cost, price) VALUES
(1, 'Linen Wrap Dress', 'Dresses', 'Ivory', 42.00, 128.00),
(2, 'Linen Wrap Dress', 'Dresses', 'Sage', 42.00, 128.00),
(3, 'Silk Slip Dress', 'Dresses', 'Black', 65.00, 185.00),
(4, 'Cropped Denim Jacket', 'Outerwear', 'Light Wash', 38.00, 110.00),
(5, 'Wool Blend Coat', 'Outerwear', 'Camel', 95.00, 295.00),
(6, 'Ribbed Knit Top', 'Tops', 'White', 12.00, 38.00),
(7, 'Ribbed Knit Top', 'Tops', 'Black', 12.00, 38.00),
(8, 'Oversized Poplin Shirt', 'Tops', 'Blue Stripe', 22.00, 68.00),
(9, 'High Rise Wide Leg Jeans', 'Bottoms', 'Indigo', 34.00, 98.00),
(10, 'Pleated Midi Skirt', 'Bottoms', 'Navy', 28.00, 84.00),
(11, 'Leather Crossbody Bag', 'Accessories', 'Cognac', 48.00, 145.00),
(12, 'Silk Scarf', 'Accessories', 'Floral', 15.00, 48.00);

CREATE TABLE inventory (
  store_id int NOT NULL,
  product_id int NOT NULL,
  quantity int,
  reorder_level int,
  PRIMARY KEY (store_id, product_id),
  FOREIGN KEY (store_id) REFERENCES stores (store_id),
  FOREIGN KEY (product_id) REFERENCES products (product_id)
);

INSERT INTO inventory (store_id, product_id, quantity, reorder_level) VALUES
(1, 1, 14, 5),
(1, 2, 3, 5),
(1, 3, 8, 3),
(1, 4, 11, 4),
(1, 5, 6, 2),
(1, 6, 25, 10),
(1, 7, 30, 10),
(1, 8, 9, 4),
(1, 9, 18, 6),
(1, 10, 7, 4),
(1, 11, 5, 3),
(1, 12, 20, 6),
(2, 1, 6, 4),
(2, 2, 9, 4),
(2, 4, 2, 4),
(2, 5, 1, 2),
(2, 6, 12, 8),
(2, 7, 4, 8),
(2, 9, 10, 5),
(2, 10, 5, 3),
(2, 11, 3, 2),
(3, 1, 4, 3),
(3, 4, 5, 3),
(3, 6, 10, 6),
(3, 7, 8, 6),
(3, 8, 2, 3),
(3, 9, 6, 4),
(3, 12, 9, 4);
