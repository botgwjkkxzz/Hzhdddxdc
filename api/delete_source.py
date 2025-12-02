from flask import Flask, request, jsonify
import json, os

SOURCE_FILE = "sources.json"
app = Flask(__name__)

def load_json(file):
    if not os.path.exists(file):
        return []
    with open(file, "r") as f:
        return json.load(f)

def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/delete_source", methods=["POST"])
def delete_source():
    data = request.json
    chat_id = data.get("chat_id")
    sources = load_json(SOURCE_FILE)
    if chat_id in sources:
        sources.remove(chat_id)
        save_json(SOURCE_FILE, sources)
    return jsonify({"status":"success","sources":sources})