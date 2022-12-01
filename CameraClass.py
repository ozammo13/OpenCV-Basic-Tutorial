import os
import cv2
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt
import time

class camera:

    cameraLink = ""
    camFeed = None

    def findCamera(self, WebcamNumber):
        print("Finding Camera...")
        self.cameraLink = WebcamNumber

    def linkCamera(self):
        self.camFeed = cv2.VideoCapture(self.cameraLink)
        print("Initializing")
        time.sleep(1)

    def readCamera(self):
        ret, frame = self.camFeed.read()
        if ret == True:
            return frame