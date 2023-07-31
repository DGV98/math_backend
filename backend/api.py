from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_session import Session
from helpers import login_required
from math_response import generate_prompt, Problem

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins":"*"}})

# Set session config
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/api/login', methods = ["POST"])
def login():
    session.clear()
    if not request.json["user_id"]:
        return jsonify("No username")
    session["user_id"] = request.json["user_id"]

    

@app.route('/api/generate', methods = ["POST"])
@login_required
def define_problem():
    category = request.json["category"]
    difficulty = request.json["difficulty"]
    p = Problem(generate_prompt(category, difficulty))
    session["problem"] = p
        
    return jsonify(next(p))

@app.route('/api/next', methods = ["GET"])
@login_required
def get_next_problem():
    return jsonify(next(session["problem"]))

@app.route('/api/logout')
def logout():
    session.clear()
    return jsonify("success")

if __name__ == "__main__":
    app.run(debug=True)