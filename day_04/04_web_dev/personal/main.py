from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def landing_page():
    return render_template('personal.html')


@app.route("/hobby/")
@app.route("/hobbies/")
def hobby():
    hobbies = ['Watching', 'Sleeping']
    return render_template('hobbies.html', hobbies=hobbies)


# @app.route("/opinion/<topic>")
# @app.route("/opinions/<topic>")
# def index(topic):
#     return f"Opinion{topic}"


@app.route("/opinion/food/")
# @app.route("/foods/")
def food():
    foods = ['Nuts', 'avocado']
    return render_template('food.html', foods=foods)

@app.route("/skills/")
def skills():
    skill_levels ={
        "Reading": "Level 1",
        "Comprehension": "Level 1",
        "Understanding": "Level 1",
    }
    return render_template("skills.html", skills=skill_levels)

app.run()
