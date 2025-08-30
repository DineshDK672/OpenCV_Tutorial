import cv2
import numpy as np


def nothing(x):
    pass


cap = cv2.VideoCapture(0)

cv2.namedWindow("Tracker")
cv2.createTrackbar("LH", "Tracker", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracker", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracker", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracker", 255, 255, nothing)
cv2.createTrackbar("US", "Tracker", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracker", 255, 255, nothing)

while True:
    # frame = cv2.imread("starry_night.jpg")    # for static photos
    _, frame = cap.read()       # for live video
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("LH", "Tracker")
    ls = cv2.getTrackbarPos("LS", "Tracker")
    lv = cv2.getTrackbarPos("LV", "Tracker")
    uh = cv2.getTrackbarPos("UH", "Tracker")
    us = cv2.getTrackbarPos("US", "Tracker")
    uv = cv2.getTrackbarPos("UV", "Tracker")

    l_b = np.array([lh, ls, lv])
    u_b = np.array([uh, us, uv])

    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Image", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", res)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
