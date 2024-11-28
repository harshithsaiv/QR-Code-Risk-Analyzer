from flask import Flask, request, jsonify
from markupsafe import escape
import numpy as np
import cv2
from pyzbar.pyzbar import decode
app = Flask(__name__)

@app.route("/decode",methods=["POST"])
def decode_qr_code():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        
        file_bytes=np.fromstring(file.read(),np.uint8)
        image=cv2.imdecode(file_bytes,cv2.IMREAD_COLOR)

        decoded_objects=decode(image)

        if not decoded_objects:
            return jsonify({"error": "No QR code found"}), 400
        
        return jsonify({"data": decoded_objects[0].data.decode("utf-8")}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == "__main__":
    app.run(debug=True)
