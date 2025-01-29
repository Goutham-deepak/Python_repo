# import mysql.connector
# conn = mysql.connector.connect(hostname='72.17.0.1 ',user='root', password='',database='MYDB')

# print(conn)  # to display the connection object




import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host='172.17.0.1',  # Corrected the parameter name and removed the trailing space
    user='goutham',
    password='goutham',  # Replace with the correct password
    database='MYDB'  # Replace with your actual database name
)

# Check the connection
if conn.is_connected():
    print("Connected to the database")
else:
    print("Failed to connect to the database")

# Optionally close the connection
conn.close()
