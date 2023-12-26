CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL
);

CREATE TABLE games (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  genre VARCHAR(255) NOT NULL,
  description VARCHAR(255) NOT NULL,
  price real NOT NULL,
  demo_file VARCHAR(255) NOT NULL,
  images VARCHAR(255) NOT NULL,
  videos VARCHAR(255) NOT NULL
);

CREATE TABLE transactions (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL,
  game_id INTEGER NOT NULL,
  price real NOT NULL,
  status VARCHAR(255) NOT NULL,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (game_id) REFERENCES games(id)
);

CREATE TABLE payments (
  id SERIAL PRIMARY KEY,
  transaction_id INTEGER NOT NULL,
  payment_method VARCHAR(255) NOT NULL,
  amount real NOT NULL,
  transaction_id_number VARCHAR(255) NOT NULL,
  FOREIGN KEY (transaction_id) REFERENCES transactions(id)
);

INSERT INTO users (name, email, password)
VALUES
('Nguyễn Văn A', 'nguyenvanan@example.com', '123456'),
('Trần Thị B', 'tranthibb@example.com', '789012'),
('Lê Quang C', 'lequangc@example.com', '345678'),
('Đỗ Thị D', 'dothdd@example.com', '901234'),
('Hoàng Văn E', 'hoangvanee@example.com', '567890');

INSERT INTO games (name, genre, description, price, demo_file, images, videos)
VALUES
('GTA 6', 'Action', 'Một trong những tựa game hành động bom tấn nhất năm 2024', 129, 'gta6_demo.zip', 'https://example.com/gta6_images', 'https://example.com/gta6_videos'),
('The Legend of Zelda: Breath of the Wild 2', 'Adventure', 'Tiếp nối câu chuyện của The Legend of Zelda: Breath of the Wild', 109.2, 'botw2_demo.zip', 'https://example.com/botw2_images', 'https://example.com/botw2_videos'),
('God of War: Ragnarok', 'Action', 'Kết thúc câu chuyện của Kratos và Atreus', 99.99, 'gowr_demo.zip', 'https://example.com/gowr_images', 'https://example.com/gowr_videos'),
('Elden Ring', 'Action RPG', 'Tựa game nhập vai hành động bom tấn của FromSoftware', 119, 'eldenring_demo.zip', 'https://example.com/eldenring_images', 'https://example.com/eldenring_videos'),
('Starfield', 'RPG', 'Tựa game nhập vai thế giới mở của Bethesda', 13.99, 'starfield_demo.zip', 'https://example.com/starfield_images', 'https://example.com/starfield_videos');

INSERT INTO transactions (user_id, game_id, price, status, created_at, updated_at)
VALUES
(1, 1, 129, 'completed', '2023-08-02 12:00:00', '2023-08-02 12:00:00'),
(2, 2, 109.2, 'completed', '2023-08-03 12:00:00', '2023-08-03 12:00:00'),
(3, 3, 99.99, 'completed', '2023-08-04 12:00:00', '2023-08-04 12:00:00'),
(4, 4, 119, 'completed', '2023-08-05 12:00:00', '2023-08-05 12:00:00'),
(5, 5, 13.99, 'completed', '2023-08-06 12:00:00', '2023-08-06 12:00:00');

INSERT INTO payments (transaction_id, payment_method, amount, transaction_id_number)
VALUES
(1, 'cash', 109.2, '1234567890123456'),
(2, 'credit card', 99.99, '9876543210987654'),
(4, 'paypal', 119, '12345678901234567890'),
(3, 'visa', 13.99, '98765432109876543210');




