# import the necessary packages
import numpy as np
import urllib
import cv2


def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # return the image
    return image


urls = [
    "https://pyimagesearch.com/wp-content/uploads/2015/01/opencv_logo.png",
    "https://pyimagesearch.com/wp-content/uploads/2015/01/google_logo.png",
    "https://pyimagesearch.com/wp-content/uploads/2014/12/adrian_face_detection_sidebar.png"
]

for url in urls:
    # download the image URL and display it
    print("downloading %s" % (url))
    image = url_to_image(url)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
