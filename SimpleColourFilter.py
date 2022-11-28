import time
import cv2 as cv
import numpy as np

# threshold
hMin = 21
sMin = 0
vMin = 0

hMax = 44
sMax = 255
vMax = 255

dim = (640, 480) #image Dimensions


# Set minimum and maximum HSV values to display
lower = np.array([hMin, sMin, vMin])
upper = np.array([hMax, sMax, vMax])

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:

    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    frame = cv.resize(frame, dim, interpolation=cv.INTER_AREA) #gets the frame size
    Colour = cv.cvtColor(frame, cv.COLOR_BGR2HSV) #turns it into a hsv
    Blur = cv.blur(Colour, [30, 30]) #blurs
    filtered = cv.inRange(Blur, lower, upper)#filters the unwanted colours
    cv.imshow('frame', filtered) #show video
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()