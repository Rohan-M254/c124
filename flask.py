from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory demonstration data. Nothing is persisted between restarts.
contacts = []
next_id = 1


@app.get("/")
def index():
    return jsonify({"message": "Contacts API"}), 200


@app.get("/contacts")
def get_contacts():
    return jsonify({"data": contacts}), 200


@app.post("/contacts")
def add_contact():
    global next_id

    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({
            "status": "error",
            "message": "A JSON object is required."
        }), 400

    name = payload.get("name")
    if not isinstance(name, str) or not name.strip():
        return jsonify({
            "status": "error",
            "message": "The 'name' field is required."
        }), 400

    contact_number = payload.get("contact", "")
    if not isinstance(contact_number, str):
        return jsonify({
            "status": "error",
            "message": "The 'contact' field must be a string."
        }), 400

    contact = {
        "id": next_id,
        "name": name.strip(),
        "contact": contact_number.strip()
    }
    contacts.append(contact)
    next_id += 1

    return jsonify({
        "status": "success",
        "data": contact
    }), 201


if __name__ == "__main__":
    app.run(debug=False)
