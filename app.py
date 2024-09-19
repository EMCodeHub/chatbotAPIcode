from flask import Flask, request, jsonify
from flask_cors import CORS

from chat import get_response

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Configuración para permitir cualquier origen

@app.route("/predict", methods=["POST"])
def predict():
    text = request.get_json().get("message")  # Asegúrate de que la clave sea "message"
    
    if not isinstance(text, str):
        return jsonify({"error": "Invalid input. Expected a string."}), 400
    
    response = get_response(text)
    message = {"answer": response}
    
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
