import cv2
import numpy as np

# events = [i for i in dir(cv2) if "EVENT" in i]        To print all events
# print(events)


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:          # Prints x, y at the point of left mouse button click
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = '('+str(x)+', '+str(y)+')'
        cv2.putText(img, text, (x, y), font, 0.4, (0, 0, 255), 1)
        cv2.imshow("Image", img)
    if event == cv2.EVENT_RBUTTONDOWN:          # Prints BGR value at the point of right mouse button click
        # Inverting x and y because in img number of rows in x and number of columns is y
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        textBGR = '('+str(blue)+', '+str(green)+', '+str(red)+')'
        cv2.putText(img, textBGR, (x, y), font, 0.4, (0, 255, 0), 1)
        cv2.imshow("Image", img)


img = cv2.imread('starry_night.jpg', 1)
if not img is None:
    cv2.imshow("Image", img)

cv2.setMouseCallback("Image", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
