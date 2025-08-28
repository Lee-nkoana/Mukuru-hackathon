# from flask import request, jsonify
# from database.UserDataBase import User, engine, Base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.exc import IntegrityError

# # Create database session
# Session = sessionmaker(bind=engine)
# db_session = Session()

# def register_user():
#     try:
#         # Get JSON data from frontend
#         data = request.get_json()
        
#         if not data:
#             return jsonify({
#                 "success": False,
#                 "message": "No data provided"
#             }), 400
        
#         username = data.get('username')
#         email = data.get('email')
#         password = data.get('password')
#         confirm_password = data.get('confirm_password')
        
#         #Validation
#         if not username or not email or not password or not confirm_password:
#             return jsonify({
#                 "success": False,
#                 "message": "All fields are required"
#             }), 400
        
#         if password != confirm_password:
#             return jsonify({
#                 "success": False,
#                 "message": "Passwords do not match"
#             }), 400
        
#         if len(password) < 6:
#             return jsonify({
#                 "success": False,
#                 "message": "Password must be at least 6 characters long"
#             }), 400
        
#         #checking if user exits
#         existing_user = db_session.query(User).filter_by(email=email).first()
#         if existing_user:
#             return jsonify({
#                 "success": False,
#                 "message": "Email already registered"
#             }), 409
        
#         #creat user
#         new_user = User(name=username, email=email, password=password)
#         db_session.add(new_user)
#         db_session.commit()
        
#         return jsonify({
#             "success": True,
#             "message": "Account created successfully",
#             "data": {
#                 "user_id": new_user.id,
#                 "username": new_user.name,
#                 "email": new_user.email
#             }
#         }), 200
        
#     except IntegrityError:
#         db_session.rollback()
#         return jsonify({
#             "success": False,
#             "message": "Email already exists"
#         }), 409
        
#     except Exception as e:
#         db_session.rollback()
#         return jsonify({
#             "success": False,
#             "message": "Registration failed"
#         }), 500

from flask import request, jsonify
from database.UserDataBase import create_user, get_user_by_email

def register_user():
    try:
        # Get JSON data from frontend
        data = request.get_json()
        
        if not data:
            return jsonify({
                "success": False,
                "message": "No data provided"
            }), 400
        
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        
        #Validation
        if not username or not email or not password or not confirm_password:
            return jsonify({
                "success": False,
                "message": "All fields are required"
            }), 400
        
        if password != confirm_password:
            return jsonify({
                "success": False,
                "message": "Passwords do not match"
            }), 400
        
        if len(password) < 6:
            return jsonify({
                "success": False,
                "message": "Password must be at least 6 characters long"
            }), 400
        
        # Check if user already exists
        existing_user = get_user_by_email(email)
        if existing_user:
            return jsonify({
                "success": False,
                "message": "Email already registered"
            }), 409
        
        # Create user in database
        new_user = create_user(username, email, password)
        if new_user is None:
            return jsonify({
                "success": False,
                "message": "Failed to create account"
            }), 500
        
        return jsonify({
            "success": True,
            "message": "Account created successfully",
            "data": {
                "user_id": new_user.id,
                "username": new_user.name,
                "email": new_user.email
            }
        }), 200
        
    except Exception as e:
        print(f"Registration error: {e}")
        return jsonify({
            "success": False,
            "message": "Registration failed"
        }), 500