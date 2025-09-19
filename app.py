from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# ✅ Correct Atlas connection
client = MongoClient(
    "mongodb+srv://rishon:vTvWY9Jwu7aKkq6g@cluster0.nq7wxuz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

db = client["flaskdb"]
collection = db["tasks"]

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        collection.insert_one({"task": task})
        return redirect(url_for("success"))
    return "Error: Task is required", 400

@app.route("/success")
def success():
    return "Data submitted successfully!"

@app.route("/get")
def get_tasks():
    tasks = list(collection.find({}, {"_id": 0}))
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(debug=True)
