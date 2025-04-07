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
