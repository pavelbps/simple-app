from flask import Flask, request, jsonify
import uuid
import logging
from flask_swagger_ui import get_swaggerui_blueprint
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--port',
                    help='set listen port',
                    required=False,
                    type=int,
                    dest='port',
                    default=5000)
args = parser.parse_args()

port = args.port
    
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

SWAGGER_URL="/docs"
API_URL="/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

users = {}

@app.route("/")
def index():
    return jsonify({"message": "Hello, World!"})

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify({"users": list(users.values())})

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Missing fields"}), 400

    user_id = str(uuid.uuid4())
    user = {
        "id": user_id,
        "name": data["name"],
        "email": data["email"]
    }

    users[user_id] = user
    return jsonify(user), 201

@app.route("/api/users/<user_id>", methods=["GET"])
def get_user(user_id):
    if user_id not in users:
        return jsonify({"error": "Not found"}), 404
    return jsonify(users[user_id])

@app.route("/api/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "Not found"}), 404
    del users[user_id]
    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
