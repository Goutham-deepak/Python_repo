# database.py
# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask
# import config

# db = SQLAlchemy()

# def create_app():
#     """Initialize Flask app and database."""
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     db.init_app(app)

#     return app

# Define the User model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)

    # def to_dict(self):
    #     return {"id": self.id, "name": self.name, "email": self.email"}









import psycopg2

# Database connection details
DB_HOST = "127.0.0.1"  # Change if needed
DB_PORT = "5603"       # Your PostgreSQL port
DB_NAME = "postgres"   # Your database name
DB_USER = "postgres"   # Your username
DB_PASSWORD = "your_password"  # Change to your actual password

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host="iot.hyperthings.in",
        port="6120",
        database="test_db",
        user="superadmin",
        password="AR6BHwxxUBmX"
    )
    
    # Create a cursor object
    cursor = conn.cursor()
    
    # Execute a simple query
    cursor.execute("SELECT version();")
    
    # Fetch and print the result
    db_version = cursor.fetchone()
    print("Connected to:", db_version)

    # Close the connection
    cursor.close()
    conn.close()

except Exception as e:
    print("Error connecting to the database:", e)
