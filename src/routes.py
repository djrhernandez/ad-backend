# routes.py
from flask import jsonify, request
from gui import calculate

def init_app(app, logger):
    @app.before_request
    def log_request_info():
        logger.info(f"Incoming request: {request}")
        
    
    @app.route('/')
    def health_check():
        data = { 'status': 'OK' }
        return jsonify(data), 200
    
    
    @app.route('/calculator', methods=['GET', 'POST'])
    def calculator():
        if request == 'GET':
            return jsonify({"message": "Send a POST request with 'expression' to evaluate"})
        
        data = request.get_json()
        expression = data.get('expression')
        if not expression:
            return jsonify({"error": "Expression is required"}), 400
        
        result = calculate(expression)
        return jsonify({"expression": expression, "result": result}), 200