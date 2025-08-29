import cv2
import numpy as np

img = cv2.imread("starry_night.jpg")
# Returns a tuple with number of rows, columns and channels in the image
if not img is None:
    print(img.shape)
    print(img.size)  # Returns that size of the image in pixels
    print(img.dtype)  # Returns the dtype of the individual pixel value in the image

    star = img[36:99, 423:490]
    # Encapsulates the copied image within a rectangle
    cv2.rectangle(img, (394, 155), (470, 225), (0, 0, 255), 3)
    img[159:222, 399:466] = star
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
