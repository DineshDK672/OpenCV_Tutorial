import cv2 as cv
import numpy as np


def nothing(x):
    print(x)


img = np.zeros((500, 500, 3), np.uint8)


cv.namedWindow("Image")

cv.createTrackbar("B", "Image", 0, 255, nothing)
cv.createTrackbar("G", "Image", 0, 255, nothing)
cv.createTrackbar("R", "Image", 0, 255, nothing)

cv.createTrackbar("ON\\OFF", "Image", 0, 1, nothing)

while (True):
    print("Inside while")
    # img = cv.imread("starry_night.jpg")
    cv.imshow("Image", img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    b = cv.getTrackbarPos("B", "Image")
    g = cv.getTrackbarPos("G", "Image")
    r = cv.getTrackbarPos("R", "Image")
    s = cv.getTrackbarPos("ON\\OFF", "Image")

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]


cv.destroyAllWindows()
