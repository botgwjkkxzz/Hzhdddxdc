from flask import Flask, request, jsonify
import json, os

TARGET_FILE = "targets.json"
app = Flask(__name__)

def load_json(file):
    if not os.path.exists(file):
        return []
    with open(file, "r") as f:
        return json.load(f)

def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/delete_target", methods=["POST"])
def delete_target():
    data = request.json
    chat_id = data.get("chat_id")
    targets = load_json(TARGET_FILE)
    if chat_id in targets:
        targets.remove(chat_id)
        save_json(TARGET_FILE, targets)
    return jsonify({"status":"success","targets":targets})