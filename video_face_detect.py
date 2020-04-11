import cv2
import os

video_file = [f for f in os.listdir('.') if f.endswith('.mp4')][0]

video = cv2.VideoCapture(video_file)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5)
    for x, y, w, h in faces:
        # image, upperleft coordinate, bottomright coordinte, color, stroke
        gray = cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow('c', gray)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
