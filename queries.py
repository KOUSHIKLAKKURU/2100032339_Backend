import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Koushi*2004",
  database="retail_store"
)
cur = conn.cursor()

# 1. List all customers
cur.execute("SELECT * FROM customers")
all_customers = cur.fetchall()
print("1)",all_customers)

# 2. Find all orders placed in January 2023
cur.execute("SELECT * FROM orders WHERE YEAR(order_date) = 2023 AND MONTH(order_date) = 1")
january_orders = cur.fetchall()
print("2)",january_orders)

# 3. Get the details of each order, including the customer name and email
cur.execute("SELECT orders.order_id, CONCAT(customers.first_name,' ',customers.last_name) AS name, customers.email FROM orders JOIN customers ON orders.customer_id = customers.customer_id")
order_details = cur.fetchall()
print("3)",order_details)

# 4. List the products purchased in a specific order (e.g., OrderID = 1)
cur.execute("SELECT products.product_name FROM order_items JOIN products ON order_items.product_id = products.product_id WHERE order_items.order_id = 1")
products_in_order = cur.fetchall()
print("4)",products_in_order)

# 5. Calculate the total amount spent by each customer
cur.execute("SELECT CONCAT(customers.first_name,' ',customers.last_name) AS customer_name, SUM(order_items.quantity * products.price) as total_spent FROM customers JOIN orders ON customers.customer_id = orders.customer_id JOIN order_items ON orders.order_id = order_items.order_id JOIN products ON order_items.product_id = products.product_id GROUP BY customers.customer_id")
total_spent = cur.fetchall()
print("5)",total_spent)

# 6. Find the most popular product (the one that has been ordered the most)
cur.execute("SELECT products.product_name, SUM(order_items.quantity) as total_quantity FROM products JOIN order_items ON products.product_id = order_items.product_id GROUP BY products.product_id ORDER BY total_quantity DESC LIMIT 1")
most_popular_product = cur.fetchall()
print("6)",most_popular_product)

# 7. Get the total number of orders and the total sales amount for each month in 2023
cur.execute("SELECT DATE_FORMAT(order_date, '%Y-%m') as month, COUNT(orders.order_id) as total_orders, SUM(order_items.quantity * products.price) as total_sales FROM orders JOIN order_items ON orders.order_id = order_items.order_id JOIN products ON order_items.product_id = products.product_id WHERE YEAR(order_date) = 2023 GROUP BY month")
monthly_sales = cur.fetchall()
print("7)",monthly_sales)

# 8. Find customers who have spent more than $1000
cur.execute("SELECT CONCAT(customers.first_name,' ',customers.last_name) AS customer_name, SUM(order_items.quantity * products.price) as total_spent FROM customers JOIN orders ON customers.customer_id = orders.customer_id JOIN order_items ON orders.order_id = order_items.order_id JOIN products ON order_items.product_id = products.product_id GROUP BY customers.customer_id HAVING total_spent > 1000")
big_spenders = cur.fetchall()
print("8)",big_spenders)

conn.close()
