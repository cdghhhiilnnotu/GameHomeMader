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
  price FLOAT(10,2) NOT NULL,
  demo_file VARCHAR(255) NOT NULL,
  images VARCHAR(255) NOT NULL,
  videos VARCHAR(255) NOT NULL
);

CREATE TABLE transactions (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL,
  game_id INTEGER NOT NULL,
  price FLOAT(10,2) NOT NULL,
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
  amount FLOAT(10,2) NOT NULL,
  transaction_id_number VARCHAR(255) NOT NULL,
  FOREIGN KEY (transaction_id) REFERENCES transactions(id)
);