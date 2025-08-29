import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)

print(cap.get(3))
print(cap.get(4))


while (cap.isOpened()):

    ret, frame = cap.read()
    if ret:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Width : " + str(cap.get(3)) + \
            " Height : " + str(cap.get(4))
        datet = str(datetime.now())
        frame = cv2.putText(frame, datet, (20, 70), font,
                            2, (0, 0, 255), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, text, (20, 130), font,
                            2, (0, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow("Video", frame)

        if cv2.waitKey(1) == ord('q'):
            cap.release()
    else:
        cap.release()

cv2.destroyAllWindows()
