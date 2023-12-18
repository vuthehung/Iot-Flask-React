from camera import Camera
from flask_cors import CORS
from flask import Flask, jsonify, request, Response
import urllib.request
import numpy as np
import os
import cv2

app = Flask(__name__)
CORS(app)

camera1 = Camera('trước cửa nhà', 'http://192.168.0.101/cam-mid.jpg')
camera2 = Camera('phòng khách', 'http://192.168.0.102/cam-mid.jpg')

@app.route('/arm', methods=['POST'])
def arm():
    camera1.arm()
    return jsonify(message="System armed."), 200

@app.route('/arm2', methods=['POST'])
def arm2():
    camera2.arm()
    return jsonify(message="System 2 armed."), 200

@app.route('/disarm', methods=['POST'])
def disarm():
    camera1.disarm()
    return jsonify(message="System disarmed."), 200

@app.route('/disarm2', methods=['POST'])
def disarm2():
    camera2.disarm()
    return jsonify(message="System 2 disarmed."), 200

@app.route('/get-armed', methods=['GET'])
def get_armed():
    return jsonify(armed=camera1.armed), 200

@app.route('/get-armed2', methods=['GET'])
def get_armed2():
    return jsonify(armed2=camera2.armed), 200

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

def generate_frames2():
    while True:
        try:
            # read the camera frame
            img_resp = urllib.request.urlopen(camera2.url)
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



@app.route('/stream2')
def stream2():
    return Response(generate_frames2(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video/<filename>')
def get_video(filename):
    video_folder = 'video' 

    full_path = os.path.join(app.root_path, video_folder, filename)

    def generate():
        with open(full_path, 'rb') as video_file:
            data = video_file.read(1024)
            while data:
                yield data
                data = video_file.read(1024)

    return Response(generate(), mimetype="video/mp4")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
