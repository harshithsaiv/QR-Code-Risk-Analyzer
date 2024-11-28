from flask import Flask, request, jsonify
from app.services.decoder import decode_qr_image

app = Flask(__name__)

@app.route("/decode", methods=["POST"])
def decode_qr_code():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        
        result = decode_qr_image(file.read())
        return jsonify({"data": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)