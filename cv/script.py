import os
import cv2

jpg_files = [f for f in os.listdir('..') if f.endswith('.jpg')]

for file in jpg_files:
    img = cv2.imread(file, 1)
    resized_img = cv2.resize(img, (100, 100))
    cv2.imwrite(file[:-4]+'resized.jpg', resized_img)
