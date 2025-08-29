from flask import request, jsonify
from database.UserDataBase import get_user_by_email
from database.Transactions import addTransaction

def transact():
    try:
        # Get JSON data from frontend
        data = request.get_json()
        
        if not data:
            return jsonify({ 
                "success": False,
                "message": "No data provided"
            }), 400
        
        # Extract required fields from client JSON
        user_email = data.get('user_email')  # User must be logged in
        reference = data.get('reference')
        recipient = data.get('recipient') 
        amount = data.get('amount')
        currency = data.get('currency')
        
        # Validate that all required fields are provided
        if not user_email or not reference or not recipient or not amount or not currency:
            return jsonify({
                "success": False,
                "message": "All fields are required: user_email, reference, recipient, amount, currency"
            }), 400
        
        # Validate amount is a number
        try:
            amount = float(amount)
            if amount <= 0:
                return jsonify({
                    "success": False,
                    "message": "Amount must be greater than 0"
                }), 400
        except ValueError:
            return jsonify({
                "success": False,
                "message": "Amount must be a valid number"
            }), 400
        
        # Check if user exists (user must be logged in)
        user = get_user_by_email(user_email)
        if not user:
            return jsonify({
                "success": False,
                "message": "User not found. Please login first."
            }), 404
        
        # Simulate transaction processing (in real app, this would call payment gateway)
        # For now, we'll assume the transaction goes through successfully
        transaction_successful = True
        
        if transaction_successful:
            # Save transaction to database
            saved_transaction = addTransaction(
                reference=reference,
                recipient=recipient,
                amount=int(amount),  # Convert to int for database
                currency=currency,
            )
            
            if saved_transaction:
                # Return transaction data in JSON format for client to display
                from datetime import datetime
                return jsonify({
                    "success": True,
                    "message": "Transaction completed successfully",
                    "transaction": {
                        "reference": reference,  # Use original reference without user_id suffix
                        "recipient": recipient,
                        "amount": int(amount),
                        "currency": currency,
                        "date": datetime.now().isoformat(),
                        "user_email": user_email
                    }
                }), 200
            else:
                return jsonify({
                    "success": False,
                    "message": "Failed to save transaction to database"
                }), 500
        
        else:
            # Handle case where money doesn't go through
            return jsonify({
                "success": False,
                "message": "Transaction failed. Insufficient funds or payment error."
            }), 400
        
    except Exception as e:
        print(f"Transaction error: {e}")
        return jsonify({
            "success": False,
            "message": "Transaction processing failed. Please try again."
        }), 500

       
       
       
       
# save all these now in the transaction database for this current user, so trnsaction table need to be linked/joined with the user table 
# if the transaction is successful, return back to the client a json format agin with this data so that they can display it in transaction history showing date, recepient, reference, amount and currency
# also do exception handling incase money doesnt go through