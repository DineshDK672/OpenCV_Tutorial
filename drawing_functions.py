import cv2
import numpy as np

img = cv2.imread("starry_night.jpg", 1)
# img = np.zeros([600, 800, 3], np.uint8)  # For a complete black image

img = cv2.line(img, (20, 20), (250, 250), (0, 0, 255), 5)
img = cv2.arrowedLine(img, (50, 50), (50, 250), (0, 255, 0), 5)
img = cv2.rectangle(img, (150, 20), (250, 250), (255, 150, 0), 5)
img = cv2.circle(img, (250, 250), 50, (10, 150, 250), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, "OpenCV", (0, 550), font,
                  6, (255, 255, 255), cv2.LINE_AA)

cv2.imshow("Draw", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
