import os
import cv2
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt
import CameraClass

#Initiates the hand class and stores it in a variable
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

Cam = CameraClass.camera()
Cam.findCamera("/dev/v4l/by-id/usb-OmniVision_Technologies__Inc._USB_Camera-B4.09.24.1-video-index0")
Cam.linkCamera()

while True:
    success, image = Cam.camFeed.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)
    # checking whether a hand is detected
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks: # working with each hand
            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 9 :
                    cv2.circle(image, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
            
            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
    cv2.imshow("Output", image)
    cv2.waitKey(1)