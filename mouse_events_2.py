import cv2
import numpy as np


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:

        # Draws a line between two clicks
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        points.append((x, y))
        if len(points) == 2:
            cv2.line(img, points[-1], points[-2], (0, 0, 255), 5)
        cv2.imshow("Image", img)

        # Shows the color of the point clicked on a different window
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        blackBG = np.zeros((512, 512, 3), np.uint8)
        blackBG[:] = [blue, green, red]
        cv2.imshow("Color", blackBG)
        cv2.waitKey(3000)
        cv2.destroyWindow("Color")


img = cv2.imread('starry_night.jpg', 1)
points = []
if not img is None:
    cv2.imshow("Image", img)

cv2.setMouseCallback("Image", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
