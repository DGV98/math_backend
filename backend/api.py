from flask import Flask, jsonify, request, session
from flask_cors import CORS
from flask_session import Session
from helpers import login_required
from math_response import generate_prompt, get_response, clean_response

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Set session config
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# @app.route("/api/login", methods=["POST"])
# def login():
#     session.clear()
#     if not request.json["user_id"]:
#         return jsonify("No username")
#     session["user_id"] = request.json["user_id"]


@app.route("/api/test", methods=["POST"])
def test():
    return jsonify({"Result": "Success " + request.json["category"]})


@app.route("/api/generate", methods=["POST"])
# @login_required
def define_problem():
    category = request.json["category"]
    difficulty = request.json["difficulty"]

    return jsonify(clean_response(get_response(generate_prompt(category, difficulty))))


# @app.route("/api/logout")
# def logout():
#     session.clear()
#     return jsonify("success")

if __name__ == "__main__":
    app.run(debug=True)
