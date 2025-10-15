from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"

# Helper functions
def load_students():
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_students(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)

# Routes
@app.route("/")
def index():
    sort_by = request.args.get("sort", "id")
    students = load_students()
    students = sorted(students, key=lambda x: x.get(sort_by, ""))
    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add_student():
    students = load_students()
    new_id = max([s["id"] for s in students], default=0) + 1
    new_student = {
        "id": new_id,
        "name": request.form["name"],
        "email": request.form["email"],
        "course": request.form["course"]
    }
    students.append(new_student)
    save_students(students)
    return redirect(url_for("index"))

@app.route("/delete/<int:student_id>")
def delete_student(student_id):
    students = load_students()
    students = [s for s in students if s["id"] != student_id]
    save_students(students)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
