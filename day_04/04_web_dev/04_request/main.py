from datetime import datetime

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    now = datetime.now()
    return render_template('introduction.html', hour=now.hour)

@app.route("/hobby/")
@app.route("/hobbies/")
def hobby():
    hobbies = ['Play Stardew', 'Write Essay', 'Casual Walk']
    return render_template('hobbies.html', hobbies=hobbies)

@app.route("/opinion/food")
def food():
    foods = ['Fried Chicken', 'Fries', 'Ice Cream']
    return render_template('food.html', foods=foods)

@app.route("/skills")
def skills():
    skill_levels = {
        "Painting": "Intermediate",
        "Dancing": "Abysmal",
        "Singing": "Poor",
        "Translation": "Proficient",
        "Eating": "Professional"
    }
    return render_template("skills.html", skills=skill_levels)

@app.get("/todo/")
def show_todo():
    if "todos" not in session:
        session["todos"] = []
    return render_template("todo.html", todos=session["todos"])

@app.post("/todo/")
def add_todo():
    if request.form["todo"]:
        session["todos"].append(request.form["todo"])
        session.modified = True
    return redirect("/todo/")

app.run()
