from flask import Flask, request, jsonify

app = Flask(__name__)

items = [
    {"id" : 1, "name" : "Item 1", "description" : "This is item 1"},
    {"id" : 2, "name" : "Item 2", "description" : "This is item 2"}
]

@app.route("/")
def home():
    return "Welcome to our TO-DO List App"

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

@app.route("/items/<int:item_id>")
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"Error" : "Item Not Found"})
    return jsonify(item)

@app.route("/items", methods=["POST"])
def create_item():
    if not request.json or not "name" in request.json:
        return jsonify({"Error" : "Item Not Found"})
    new_item = {
        "id" : items[-1]["id"] + 1 if items else 1,
        "name" : request.json["name"],
        "description" : request.json["description"]
    }
    items.append(new_item)
    return jsonify(new_item)

@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"Error" : "Item Not Found"})
    item["name"] = request.json.get("name", item["name"])
    item["description"] = request.json.get("description", item["description"])
    return jsonify(item)

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"Result" : "Item Deleted"})

if __name__ == "__main__":
    app.run(debug=True)