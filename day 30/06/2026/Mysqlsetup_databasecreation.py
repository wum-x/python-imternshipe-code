# MySQL Setup and Database Creation in Python

# Import MySQL connector
import mysql.connector

# Connect to MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password"
)

# Create a cursor
cursor = connection.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS college")

# Display message
print("Database created successfully!")

# Close cursor
cursor.close()
# Import MySQL connector
import mysql.connector

# Connect to the college database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

# Create cursor
cursor = connection.cursor()

print("Connected to college database successfully!")

# Close cursor and connection
cursor.close()
connection.close()

# Close connection
connection.close()

print("MySQL connection closed.")
# Import MySQL connector
import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

# Create cursor
cursor = connection.cursor()

# SQL query to create a students table
query = """
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100)
)
"""

# Execute the query
cursor.execute(query)

# Save changes
connection.commit()

print("Students table created successfully!")

# Close connection
cursor.close()
connection.close()

