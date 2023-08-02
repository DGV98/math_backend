from flask import Flask, jsonify, request, session
from flask_cors import CORS
from flask_session import Session
from math_response import generate_prompt, get_response, clean_response

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/api/generate", methods=["POST"])
def define_problem():
    category = request.json["category"]
    difficulty = request.json["difficulty"]
    return jsonify(clean_response(get_response(generate_prompt(category, difficulty))))


# if __name__ == "__main__":
#     app.run(debug=True)
