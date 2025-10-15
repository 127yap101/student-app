from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

DATA_FILE = "data.json"

def load_students():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_students(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)

@app.route("/")
def index():
    sort_by = request.args.get("sort", "id")
    students = load_students()
    students = sorted(students, key=lambda x: x.get(sort_by, ""))
    return render_template("index.html", students=students)

@app.route("/delete/<int:student_id>")
def delete_student(student_id):
    students = load_students()
    students = [s for s in students if s["id"] != student_id]
    save_students(students)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
