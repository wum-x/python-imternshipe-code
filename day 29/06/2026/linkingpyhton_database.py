# Linking Python with MySQL Database

# Import MySQL connector
import mysql.connector

# Connect Python to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

# Check whether connection is successful
if connection.is_connected():
    print("Python connected to MySQL successfully!")

# Create cursor
cursor = connection.cursor()

# Execute SQL query
cursor.execute("SELECT * FROM students")

# Get all records
records = cursor.fetchall()

# Display records
for row in records:
    print(row)

# Close cursor
cursor.close()

# Close database connection
connection.close()

print("Database connection closed.")
