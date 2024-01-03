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
  price INT(10) NOT NULL,
  demo_file VARCHAR(255) NOT NULL,
  images VARCHAR(255) NOT NULL,
  videos VARCHAR(255) NOT NULL
);    

CREATE TABLE transactions (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL,
  game_id INTEGER NOT NULL,
  price INT(10) NOT NULL,
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
  amount INT(10) NOT NULL,
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
('GTA 5', 'Action', 'Một trong những tựa game hành động bom tấn.', 1290000, 'gta6_demo.zip', 'https://wallpaperfx.com/view_image/new-grand-theft-auto-v-1920x1080-wallpaper-13675.jpg', 'https://www.youtube.com/watch?v=QkkoHAzjnUs'),
('Cyberpunk 2077', 'Action RPG', 'Trò chơi hành động nhập vai nổi bật với bối cảnh Cyberpunk, mang đến trải nghiệm độc đáo trong thế giới công nghệ cao và tương lai đen tối.', 1090000, 'botw2_demo.zip', 'https://gamingnerd.net/wp-content/uploads/2023/09/th-99200-36698.jpg', 'https://www.youtube.com/watch?v=Ugb80d5lxEM'),
('God of War Ragnarok', 'Action', 'Kết thúc câu chuyện của Kratos và Atreus', 990000, 'gowr_demo.zip', 'https://wallpapers.com/images/featured/god-of-war-83rush6v76r4v0ul.jpg', 'https://youtu.be/hfJ4Km46A-0?si=n3FBtOsd-0dmA3r9'),
('Elden Ring', 'Action RPG', 'Tựa game nhập vai hành động bom tấn của FromSoftware', 1190000, 'eldenring_demo.zip', 'https://wallpapercave.com/wp/wp4674107.jpg', 'https://youtu.be/E3Huy2cdih0?si=PVxq268m7qVMZq-K'),
('Among Us', 'Social Deduction', 'Among Us là một trò chơi nhiệm vụ đa người chơi nổi tiếng, nơi người chơi phải tìm ra kẻ giết người hoặc hoàn thành nhiệm vụ trước khi bị loại khỏi game.', 1390000, 'starfield_demo.zip', 'https://wallpapers.com/images/hd/among-us-space-background-l9i6kd6ax4uj7o0v.jpg', 'https://youtu.be/9pyYq9lpjls?si=4fdfLjvnpu3IvEvW');

INSERT INTO transactions (user_id, game_id, price, status, created_at, updated_at)
VALUES
(1, 1, 1290000, 'completed', '2023-08-02 12:00:00', '2023-08-02 12:00:00'),
(2, 2, 1090000, 'completed', '2023-08-03 12:00:00', '2023-08-03 12:00:00'),
(3, 3, 990000, 'completed', '2023-08-04 12:00:00', '2023-08-04 12:00:00'),
(4, 4, 1190000, 'completed', '2023-08-05 12:00:00', '2023-08-05 12:00:00'),
(5, 5, 1390000, 'completed', '2023-08-06 12:00:00', '2023-08-06 12:00:00');

INSERT INTO payments (transaction_id, payment_method, amount, transaction_id_number)
VALUES
(1, 'cash', 1090000, '1234567890123456'),
(2, 'credit card', 990000, '9876543210987654'),
(4, 'paypal', 1190000, '12345678901234567890'),
(3, 'visa', 1390000, '98765432109876543210');
