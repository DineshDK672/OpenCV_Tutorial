import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 40.0, (1920, 1080))

print(cap.get(3))
print(cap.get(4))

while (cap.isOpened()):

    ret, frame = cap.read()
    if ret:

        cap.set(3, 720)  # Code 3 is for width
        cap.set(4, 480)  # Code 4 is for width

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # For greyscale image
        cv2.imshow("Video Capture", gray)

        if cv2.waitKey(1) == ord('q'):
            cap.release()
    else:
        cap.release()

out.release()
cv2.destroyAllWindows()
