import os
import cv2
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt
import CameraClass

#Initiates the hand class and stores it in a variable
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.3)
mp_drawing = mp.solutions.drawing_utils

Cam = CameraClass.camera()
Cam.findCamera("Video1")
Cam.linkCamera()

while True:
    frame = Cam.readCamera()
    cv2.imshow("ahh", frame)
