from flask import Flask, jsonify
import json, os

SOURCE_FILE = "sources.json"
app = Flask(__name__)

@app.route("/sources", methods=["GET"])
def get_sources():
    if not os.path.exists(SOURCE_FILE):
        return jsonify([])
    with open(SOURCE_FILE, "r") as f:
        sources = json.load(f)
    return jsonify(sources)