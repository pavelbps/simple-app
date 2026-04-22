from flask import Flask, request, jsonify
import uuid
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

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
    app.run(host="0.0.0.0", port=5000)
