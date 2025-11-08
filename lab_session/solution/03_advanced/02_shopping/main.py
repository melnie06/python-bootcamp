from flask import Flask, session, request, redirect, render_template

app = Flask(__name__)
app.secret_key = "replace-with-a-secure-key"  # CHANGE THIS in production


@app.get("/")
@app.get("/shopping/")
def show_shopping_list():
    if "items" not in session:
        session["items"] = []
    return render_template("shopping.html", items=session["items"])


@app.post("/shopping/")
def add_item_to_list():
    item = request.form.get("item", "").strip()
    if item:
        session["items"].append(item)
        session.modified = True
    return redirect("/shopping/")


@app.post("/shopping/delete/<int:index>")
def delete_item(index):
    if "items" in session and 0 <= index < len(session["items"]):
        session["items"].pop(index)
        session.modified = True
    return redirect("/shopping/")


app.run()
