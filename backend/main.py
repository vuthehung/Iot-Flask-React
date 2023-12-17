from camera import Camera
from flask_cors import CORS
from flask import Flask, jsonify, request, render_template, Response, send_file, send_from_directory
from db import init_db
import urllib.request
import numpy as np
import os
import cv2

app = Flask(__name__)
CORS(app)
app.config["MYSQL_DATABASE_HOST"]='localhost'
app.config["MYSQL_DATABASE_USER"]="root"
app.config["MYSQL_DATABASE_PASSWORD"]="1"
app.config["MYSQL_DATABASE_DB"]='iot'

init_db(app)

camera1 = Camera()
@app.route('/arm', methods=['POST'])
def arm():
    camera1.arm()
    return jsonify(message="System armed."), 200

@app.route('/disarm', methods=['POST'])
def disarm():
    camera1.disarm()
    return jsonify(message="System disarmed."), 200

@app.route('/get-armed', methods=['GET'])
def get_armed():
    return jsonify(armed=camera1.armed), 200


def generate_frames():
    while True:
        try:
            # read the camera frame
            img_resp = urllib.request.urlopen(camera1.url)
            img_np = np.array(bytearray(img_resp.read()), dtype=np.uint8)
            frame = cv2.imdecode(img_np, -1)

            # encode as a JPEG image and return it
            ret, jpeg = cv2.imencode('.jpg', frame)
            if not ret:
                continue

            frame_bytes = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

        except Exception as e:
            print(f"Error: {e}")


@app.route('/stream')
def stream():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)