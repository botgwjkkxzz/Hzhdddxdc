from flask import Flask, jsonify
import json, os

TARGET_FILE = "targets.json"
app = Flask(__name__)

@app.route("/targets", methods=["GET"])
def get_targets():
    if not os.path.exists(TARGET_FILE):
        return jsonify([])
    with open(TARGET_FILE, "r") as f:
        targets = json.load(f)
    return jsonify(targets)