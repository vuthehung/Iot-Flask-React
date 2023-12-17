import cv2 as cv
import time
import numpy as np
import os
import urllib.request
import threading
import datetime
from database import connect_to_database, insert_video_record, close_connection
from sentoTelegram import send_notification_with_video

class Camera:
    net = cv.dnn.readNetFromCaffe('models/config.txt', 'models/mobilenet_iter_73000.caffemodel')
    url = 'http://192.168.0.107/cam-mid.jpg'
    cap = None
    out = None
    db_connection = None

    def __init__(self):
        self.armed = False
        self.camera_thread = None
        self.db_connection = connect_to_database()
    
    def arm(self):
        if not self.armed and not self.camera_thread:
            self.camera_thread = threading.Thread(target=self.run)
        
        self.camera_thread.start()
        self.armed = True
        print("Camera armed.")

    def disarm(self):
        self.armed = False
        self.camera_thread = None
        close_connection(self.db_connection)
        print("Camera disarmed.")

    def run(self):
        person_detected = False
        non_detected_counter = 0
        current_recording_name = None
        video_name = None
        datetimeDetect = None

        Camera.cap = cv.VideoCapture(Camera.url)

        print("Camera started...")
        while self.armed:
            img_resp = urllib.request.urlopen(Camera.url)
            imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
            frame = cv.imdecode(imgnp, -1)
            blob = cv.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
            self.net.setInput(blob)
            detections = self.net.forward()
            person_detected = False

            for i in range(detections.shape[2]):
                # Extract the confidence
                confidence = detections[0, 0, i, 2]

                # Get the label for the class number and set its color
                idx = int(detections[0, 0, i, 1])

                # Check if the detection is of a person and its confidence is greater than the minimum confidence
                if idx == 15 and confidence > 0.5:
                    box = detections[0, 0, i, 3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
                    (startX, startY, endX, endY) = box.astype("int")
                    cv.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                    person_detected = True

            # If a person is detected, start/continue recording
            if person_detected:
                non_detected_counter = 0  # reset the counter
                if self.out is None:  # if VideoWriter isn't initialized, initialize it
                    now = datetime.datetime.now()
                    formatted_now = now.strftime("%d-%m-%y-%H-%M-%S")
                    print("Person motion detected at", formatted_now)
                    video_name = f'{formatted_now}.mp4'
                    photo_name = f'{formatted_now}.jpg'
                    current_recording_name = os.path.join('video', video_name)
                    photo_path = os.path.join('anh', photo_name) 
                    datetimeDetect = now.strftime("%Y-%m-%d %H:%M:%S")
                    fourcc = cv.VideoWriter_fourcc(*'mp4v')  
                    self.out = cv.VideoWriter(current_recording_name, fourcc, 20.0, (frame.shape[1], frame.shape[0]))

                    cv.imwrite(photo_path, frame)
                    # insert_video_record(self.db_connection, current_recording_name, datetimeDetect)
                

                self.out.write(frame)

            # If no person is detected, stop recording after 50 frames
            else:
                non_detected_counter += 1  # increment the counter
                if non_detected_counter >= 20:  # if 50 frames have passed without a detection
                    if self.out is not None:  # if VideoWriter is initialized, release it
                        self.out.release()
                        self.out = None  # set it back to None
                        thread = threading.Thread(target=send_notification_with_video, args=(current_recording_name,datetimeDetect,))
                        thread.start()
                        current_recording_name = None

            cv.imshow('Image', frame)  
            cv.waitKey(1)    
        if self.out is not None:  # if VideoWriter is initialized, release it
            self.out.release()
            self.out = None  # set it back to None
            current_recording_name = None
            
        self.cap.release()
        print("Camera released...")

    def __del__(self):
        self.cap.release()
        if self.out is not None:
            self.out.release()
