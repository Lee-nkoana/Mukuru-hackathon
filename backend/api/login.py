from flask import request, jsonify
from database.UserDataBase import get_user_by_email

def user_login():
    try:
        # Get JSON data from frontend
        data = request.get_json()
        
        if not data:
            return jsonify({
                "success": False,
                "message": "No data provided"
            }), 400
        
    
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({
                "success": False,
                "message": "email and passowrd are required"
            }), 400

        user = get_user_by_email(email)

        if user is None:
            return jsonify({
                "success": False,
                "message": "User does not exist"
            }), 404

        if user.password != password:
            return jsonify({
                "success": False,
                "message":"Invalid passowrd"
            }), 401

        return jsonify({
            "success": True,
            "message": "Login successful",
            "data": {
                "user_id": user.id,
                "username": user.name,
                "email": user.email
            }
            }), 200
        
    except Exception as e:
         return jsonify({
            "success":False,
            "message": "login failed"
        }), 500



#         if user does not exist on the database:
#             return message:user does not exist and message should be json format

# otherwise, open the user(from database) after checking that email does not exists(unique identifier  for database)
# then rnder profile.html and return the username, 