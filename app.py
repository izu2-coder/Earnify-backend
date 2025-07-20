from flask import Flask, jsonify, request

app = Flask(__name__)

 # Mock data for tasks
 tasks_db = [ 
     {"id": 1, "title": "Complete Survey", "location": "Lagos", "price": "₦500"},
     {"id": 2, "title": "Share Post", "location": "Remote", "price": "₦300"}, 
     {"id": 3, "title": "Install App", "location": "Abuja", "price": "₦700"},
     {"id": 4, "title": "Refer Friend", "location": "Nationwide", "price": "₦10K"}, 
     {"id": 5, "title": "Rate Product", "location": "Lagos", "price": "₦600"} 
 ]

 @app.route('/api/tasks', methods=['GET']) 
def get_tasks(): 
         return jsonify({"tasks": tasks_db}), 200

 @app.route('/api/health', methods=['GET']) 
def health_check(): 
         return jsonify({"status": "Backend is running!"}), 200 

if __name__ == '__main__':
 app.run(debug=True)
