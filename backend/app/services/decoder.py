import cv2
import numpy as np
from pyzbar.pyzbar import decode

def decode_qr_image(file_bytes):
    image = cv2.imdecode(np.fromstring(file_bytes, np.uint8), cv2.IMREAD_COLOR)
    decoded_objects = decode(image)
    
    if not decoded_objects:
        raise ValueError("No QR code found")
        
    return decoded_objects[0].data.decode("utf-8") 