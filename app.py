from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DATA_FILE = "data.json"

# Initialize JSON file
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        roll = request.form.get("roll")
        email = request.form.get("email")
        student = {"name": name, "roll": roll, "email": email}

        # Read existing data
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        data.append(student)

        # Write updated data
        with open(DATA_FILE, "w") as f:
            json.dump(data, f)

        return redirect(url_for("index"))

    # GET request → display students
    with open(DATA_FILE, "r") as f:
        students = json.load(f)
    return render_template("index.html", students=students)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
