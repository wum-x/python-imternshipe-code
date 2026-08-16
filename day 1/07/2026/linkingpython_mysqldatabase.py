# ==========================================
# LINKING PYTHON WITH MYSQL DATABASE
# ==========================================

# Import MySQL connector
import mysql.connector

try:
    # Connect Python with MySQL
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="college"
    )

    # Check connection
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

except mysql.connector.Error as error:
    # Handle database error
    print("Database Error:", error)

finally:
    # Close cursor and connection
    if 'cursor' in locals():
        cursor.close()

    if 'connection' in locals() and connection.is_connected():
        connection.close()

    print("MySQL connection closed.")
