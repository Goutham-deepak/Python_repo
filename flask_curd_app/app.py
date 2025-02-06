# # app.py
# from flask import Flask
# from database import create_app, db
# from routes import routes

# app = create_app()

# # Register Blueprint for routes
# app.register_blueprint(routes)

# # Create tables before the first request
# with app.app_context():
#     db.create_all()

# if __name__ == '__main__':
#     app.run(debug=True)
