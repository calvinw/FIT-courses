CREATE TABLE channels (
  channel_id int NOT NULL,
  channel_name varchar(50) NOT NULL,
  PRIMARY KEY (channel_id)
);

INSERT INTO channels (channel_id, channel_name) VALUES
(1, 'email'),
(2, 'web'),
(3, 'social'),
(4, 'referral'),
(5, 'push_notification'),
(6, 'sms'),
(7, 'in_app'),
(8, 'direct_mail');

CREATE TABLE users (
  user_id int NOT NULL,
  signup_date date,
  name varchar(100),
  email varchar(100),
  address varchar(255),
  PRIMARY KEY (user_id)
);

INSERT INTO users (user_id, signup_date, name, email, address) VALUES
(101, '2023-01-05', 'Alice Johnson', 'alice.johnson@example.com', '592 Birch Ln, Rivertown, FL'),
(102, '2023-02-10', 'Bob Smith', 'bob.smith@example.com', '964 Pine Rd, Hilldale, NY'),
(103, '2023-03-15', 'Charlie Kim', 'charlie.kim@example.com', '137 Cedar Blvd, Lakeview, TX'),
(104, '2023-04-20', 'Diana Lopez', 'diana.lopez@example.com', '816 Birch Ln, Brookside, NY'),
(105, '2023-05-01', 'Ethan Zhang', 'ethan.zhang@example.com', '594 Maple Ave, Brookside, TX'),
(106, '2023-06-08', 'Fiona Blake', 'fiona.blake@example.com', '110 Maple Ave, Springfield, CA'),
(107, '2023-07-12', 'George White', 'george.white@example.com', '375 Oak St, Lakeview, IL'),
(108, '2023-08-19', 'Hannah Liu', 'hannah.liu@example.com', '842 Pine Rd, Hilldale, NY'),
(109, '2023-09-05', 'Isaac Perez', 'isaac.perez@example.com', '219 Cedar Blvd, Brookside, TX'),
(110, '2023-10-01', 'Jenna Nguyen', 'jenna.nguyen@example.com', '728 Oak St, Rivertown, FL'),
(111, '2023-11-10', 'Kevin Brown', 'kevin.brown@example.com', '456 Oak Ave, Springfield, IL'),
(112, '2023-12-01', 'Laura Garcia', 'laura.garcia@example.com', '789 Pine St, Lakeview, CA'),
(113, '2024-01-18', 'Mike Davis', 'mike.davis@example.com', '101 Cedar Rd, Hilldale, TX'),
(114, '2024-02-22', 'Nancy Rodriguez', 'nancy.rodriguez@example.com', '212 Birch Blvd, Rivertown, NY'),
(115, '2024-03-30', 'Oscar Martinez', 'oscar.martinez@example.com', '323 Maple Ln, Brookside, FL'),
(116, '2024-04-05', 'Pamela Wilson', 'pamela.wilson@example.com', '434 Pine Ave, Springfield, TX'),
(117, '2024-05-11', 'Quentin Taylor', 'quentin.taylor@example.com', '545 Oak St, Lakeview, NY'),
(118, '2024-06-16', 'Rachel Thomas', 'rachel.thomas@example.com', '656 Cedar Blvd, Hilldale, CA'),
(119, '2024-07-20', 'Steve Jackson', 'steve.jackson@example.com', '767 Birch Ln, Rivertown, TX'),
(120, '2024-08-25', 'Tina White', 'tina.white@example.com', '878 Maple Rd, Brookside, NY');

CREATE TABLE interactions (
  interaction_id int NOT NULL,
  user_id int,
  channel_id int,
  campaign varchar(100),
  opened_email tinyint,
  clicked_link tinyint,
  session_duration int,
  pages_visited int,
  converted tinyint,
  PRIMARY KEY (interaction_id),
  FOREIGN KEY (user_id) REFERENCES users (user_id),
  FOREIGN KEY (channel_id) REFERENCES channels (channel_id)
);

INSERT INTO interactions (interaction_id, user_id, channel_id, campaign, opened_email, clicked_link, session_duration, pages_visited, converted) VALUES
(1, 101, 1, 'Spring Sale', 1, 1, NULL, NULL, 0),
(2, 102, 1, 'Spring Sale', 0, 0, NULL, NULL, 0),
(3, 103, 2, 'Homepage Visit', NULL, 1, 300, 5, 1),
(4, 104, 2, 'Product Launch', NULL, 1, 180, 3, 1),
(5, 105, 3, 'Instagram Story', NULL, 1, 60, 1, 0),
(8, 108, 4, 'Partner Blog', NULL, 1, 90, 2, 1),
(9, 109, 2, 'Category Page', NULL, 1, 220, 4, 1),
(13, 105, 4, 'Referral Discount', NULL, 1, 30, 1, 1),
(16, 102, 2, 'Homepage Visit', NULL, 1, 150, 3, 1),
(17, 102, 3, 'Instagram Story', NULL, 1, 60, 1, 0),
(18, 108, 2, 'Product Page', NULL, 1, 200, 4, 1),
(19, 110, 2, 'Category Page', NULL, 1, 180, 3, 1),
(20, 101, 3, 'Social Flash', NULL, 1, 40, 1, 0),
(23, 106, 2, 'Homepage Visit', NULL, 1, 310, 5, 1),
(26, 101, 5, 'New Feature Alert', NULL, 1, NULL, NULL, 0),
(31, 106, 1, 'Flash Sale SMS', NULL, 1, NULL, NULL, 1),
(33, 108, 8, 'Holiday Catalog', 1, 1, NULL, NULL, 1),
(36, 101, 7, 'In-App Message', NULL, 1, 90, 2, 0),
(41, 102, 5, 'Push Notification', NULL, 1, NULL, NULL, 1),
(45, 101, 1, 'SMS Promo', NULL, 1, NULL, NULL, 1),
(48, 106, 8, 'Direct Mail Coupon', 1, 1, NULL, NULL, 1),
(51, 106, 3, 'Summer Promo', NULL, 1, 50, 1, 0),
(53, 103, 5, 'Flash Sale Alert', NULL, 1, NULL, NULL, 1),
(55, 101, 8, 'Holiday Catalog', 1, 0, NULL, NULL, 0),
(56, 101, 1, 'Spring Sale', 1, 0, 120, 3, 0),
(57, 102, 2, 'Homepage Visit', 0, 0, 60, 1, 0),
(58, 103, 3, 'Product Launch', 1, 1, 300, 5, 1),
(59, 104, 4, 'Instagram Story', 0, 1, 90, 2, 0),
(60, 105, 5, 'Partner Blog', 1, 0, 180, 4, 0),
(61, 106, 1, 'Category Page', 0, 0, 75, 2, 0),
(62, 107, 2, 'Referral Discount', 1, 1, 250, 6, 1),
(63, 108, 3, 'Product Page', 0, 1, 110, 3, 0),
(64, 109, 4, 'Social Flash', 1, 0, 150, 4, 0),
(65, 110, 5, 'New Feature Alert', 0, 0, 50, 1, 0),
(66, 111, 1, 'Flash Sale SMS', 1, 1, 280, 7, 1),
(67, 112, 2, 'Holiday Catalog', 0, 1, 100, 3, 0),
(68, 113, 3, 'In-App Message', 1, 0, 200, 5, 0),
(69, 114, 4, 'Push Notification', 0, 0, 40, 1, 0),
(70, 115, 1, 'SMS Promo', 1, 1, 320, 8, 1),
(71, 116, 1, 'Direct Mail Coupon', 0, 1, 130, 4, 0),
(72, 117, 2, 'Summer Promo', 1, 0, 170, 5, 0),
(73, 118, 3, 'Flash Sale Alert', 0, 0, 65, 2, 0),
(74, 119, 4, 'Spring Sale', 1, 1, 290, 6, 1),
(75, 120, 5, 'Homepage Visit', 0, 1, 85, 3, 0),
(81, 101, 1, 'Product Page', 0, 0, 70, 2, 0),
(82, 102, 2, 'Social Flash', 1, 1, 270, 6, 1),
(83, 103, 3, 'New Feature Alert', 0, 1, 95, 3, 0),
(84, 104, 1, 'Flash Sale SMS', 1, 0, 230, 5, 0),
(85, 105, 5, 'Holiday Catalog', 0, 0, 45, 1, 0),
(86, 106, 1, 'In-App Message', 1, 1, 330, 8, 1),
(87, 107, 2, 'Push Notification', 0, 1, 115, 4, 0),
(88, 108, 1, 'SMS Promo', 1, 0, 160, 5, 0),
(89, 109, 4, 'Direct Mail Coupon', 0, 0, 80, 2, 0),
(90, 110, 5, 'Summer Promo', 1, 1, 260, 6, 1),
(91, 111, 1, 'Flash Sale Alert', 0, 1, 105, 3, 0),
(92, 112, 2, 'Spring Sale', 1, 0, 220, 5, 0),
(93, 113, 3, 'Homepage Visit', 0, 0, 60, 1, 0),
(94, 114, 4, 'Product Launch', 1, 1, 300, 7, 1),
(95, 115, 5, 'Instagram Story', 0, 1, 90, 2, 0),
(96, 116, 1, 'Partner Blog', 1, 0, 180, 4, 0),
(97, 117, 2, 'Category Page', 0, 0, 75, 2, 0),
(98, 118, 3, 'Referral Discount', 1, 1, 250, 6, 1),
(99, 119, 4, 'Product Page', 0, 1, 110, 3, 0),
(100, 120, 5, 'Social Flash', 1, 0, 150, 4, 0),
(101, 101, 1, 'New Feature Alert', 0, 0, 50, 1, 0),
(102, 102, 1, 'Flash Sale SMS', 1, 1, 280, 7, 1),
(103, 103, 3, 'Holiday Catalog', 0, 1, 100, 3, 0),
(104, 104, 4, 'In-App Message', 1, 0, 200, 5, 0),
(105, 105, 5, 'Push Notification', 0, 0, 40, 1, 0),
(106, 106, 1, 'SMS Promo', 1, 1, 320, 8, 1),
(107, 107, 2, 'Direct Mail Coupon', 0, 1, 130, 4, 0),
(108, 108, 3, 'Summer Promo', 1, 0, 170, 5, 0),
(109, 109, 4, 'Flash Sale Alert', 0, 0, 65, 2, 0),
(110, 110, 5, 'Spring Sale', 1, 1, 290, 6, 1),
(111, 111, 1, 'Homepage Visit', 0, 1, 85, 3, 0),
(112, 112, 2, 'Product Launch', 1, 0, 210, 5, 0),
(113, 113, 3, 'Instagram Story', 0, 0, 55, 1, 0),
(114, 114, 4, 'Partner Blog', 1, 1, 310, 7, 1),
(115, 115, 5, 'Category Page', 0, 1, 125, 4, 0),
(116, 116, 1, 'Referral Discount', 1, 0, 190, 5, 0),
(117, 117, 2, 'Product Page', 0, 0, 70, 2, 0),
(118, 118, 3, 'Social Flash', 1, 1, 270, 6, 1),
(119, 119, 4, 'New Feature Alert', 0, 1, 95, 3, 0),
(120, 120, 1, 'Flash Sale SMS', 1, 0, 230, 5, 0);

CREATE VIEW conversion_rate_per_channel AS
SELECT
  c.channel_name,
  SUM(i.converted) AS total_conversions,
  COUNT(i.interaction_id) AS total_interactions,
  SUM(i.converted) * 100.0 / COUNT(i.interaction_id) AS conversion_rate
FROM interactions i
JOIN channels c ON i.channel_id = c.channel_id
GROUP BY c.channel_name
ORDER BY conversion_rate DESC;

CREATE VIEW conversion_rate_per_campaign AS
SELECT
  campaign,
  SUM(converted) AS total_conversions,
  COUNT(*) AS total_interactions,
  SUM(converted) * 100.0 / COUNT(*) AS conversion_rate
FROM interactions
GROUP BY campaign
ORDER BY conversion_rate DESC;

CREATE VIEW conversion_rate_per_customer AS
SELECT
  u.name,
  SUM(i.converted) AS total_conversions,
  COUNT(i.interaction_id) AS total_interactions,
  SUM(i.converted) * 100.0 / COUNT(i.interaction_id) AS conversion_rate
FROM interactions i
JOIN users u ON i.user_id = u.user_id
GROUP BY u.name
ORDER BY conversion_rate DESC;

CREATE VIEW user_total_interactions AS
SELECT u.name, COUNT(i.interaction_id) AS total_interactions
FROM interactions i
JOIN users u ON i.user_id = u.user_id
GROUP BY u.name
ORDER BY total_interactions DESC;
