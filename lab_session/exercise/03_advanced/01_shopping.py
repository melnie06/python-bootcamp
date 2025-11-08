"""
Simple Shopping List App (Flask Session Edition)

This exercise guides you through creating a basic shopping list web app using Flask.
Users will be able to:
- View their shopping list
- Add items to the list

You will store the data inside the Flask session so it persists during the user's session.
No database required.

Don't use global variables.
Do everything using session, form handling, and template rendering.
"""

from flask import Flask

app = Flask(__name__)
app.secret_key = "replace-with-a-secure-key"


@app.get("/shopping/")
def show_shopping_list():
    """
    Display the current shopping list stored in session.

    - If session["items"] doesn't exist yet, initialize it as an empty list.
    - Pass the items list to the template for display.

    Returns:
        HTML page showing all items in the shopping list.
    """
    # TODO: Check if "items" key exists in session. If not, initialize it as an empty list.

    # TODO: Return a rendered template (e.g., "shopping.html") and pass the list as a variable.
    pass


@app.post("/shopping/")
def add_item_to_list():
    """
    Handle the form submission to add a new item.

    - Get the "item" field from request.form.
    - If the item name is not empty, append it to session["items"].
    - Remember to set session.modified = True after modifying the list.

    Returns:
        Redirect back to the shopping list page.
    """
    # TODO: Get item name from form input using request.form["item"].

    # TODO: Append the item to session["items"] if it's not empty.

    # TODO: Set session.modified = True so Flask knows the list was updated.

    # TODO: Redirect back to "/shopping/"
    pass


# BONUS TODOs (Add these routes once the student finishes the basic app):

@app.post("/shopping/delete/<int:index>")
def delete_item(index: int):
    """
    BONUS: Delete an item from the shopping list by its index.

    - Use session["items"].pop(index) to remove the item.
    - Don't forget session.modified = True.

    Returns:
        Redirect back to the shopping list.
    """
    # TODO: Implement this if you want to add delete functionality.
    pass


@app.post("/shopping/bought/<int:index>")
def mark_item_as_bought(index: int):
    """
    BONUS: Mark an item as bought (advanced).

    - Update session["items"][index] to include a 'bought' flag.
    - This requires storing items as dictionaries, not just strings.
        Example: {"name": "Milk", "bought": False}

    Returns:
        Redirect back to the shopping list.
    """
    # TODO: Convert item list to use dictionaries to support more info per item.
    # TODO: Toggle the 'bought' status when this route is called.
    pass


if __name__ == "__main__":
    app.run(debug=True)
