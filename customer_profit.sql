CREATE TABLE customers (
  customer_id TEXT PRIMARY KEY,
  customer_name TEXT
);

CREATE TABLE orders (
  order_id TEXT PRIMARY KEY,
  customer_id TEXT NOT NULL,
  order_date TEXT,
  ship_mode TEXT,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
  order_id TEXT NOT NULL,
  product_id TEXT NOT NULL,
  sales REAL,
  profit REAL,
  quantity INTEGER,
  discount REAL,
  PRIMARY KEY (order_id, product_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE products (
  product_id TEXT PRIMARY KEY,
  product_name TEXT,
  category TEXT,
  sub_category TEXT
);
