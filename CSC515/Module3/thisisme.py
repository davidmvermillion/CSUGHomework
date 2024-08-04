# Import packages
import cv2
from os import chdir
from os.path import abspath, dirname, join

# Force script execution directory to current path
# https://stackoverflow.com/a/69556612/13801562
chdir(dirname(abspath(__file__)))

# Import image
image = cv2.imread('DMV.png')

# Tutorial for facial recognition: https://www.datacamp.com/tutorial/face-detection-python-opencv
# Check image shape. Results: (2544, 3342, 3)
print(image.shape)

cv2.imshow('Original Image', image)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load classifiers
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

# Detect my face
face = face_classifier.detectMultiScale(
    gray,
    scaleFactor = 1.1,
    minNeighbors = 5,
    minSize = (40, 40)
)

faces = face_classifier.detectMultiScale(gray, 1.3, 4)

# Create box around my face
for (x, y, w, h) in faces:
    cv2.rectangle(image,
                  (x, y),
                  (x + w, y + h),
                  (0, 255, 0),
                  10)

# Detect eyes
# Tutorial: https://www.tutorialspoint.com/how-to-detect-eyes-in-an-image-using-opencv-python
# loop over the detected faces
for (x,y,w,h) in face:
   roi_gray = gray[y:y+h, x:x+w]
   roi_color = image[y:y+h, x:x+w]
   
   # detects eyes of within the detected face area (roi)
   eyes = eye_cascade.detectMultiScale(roi_gray)
   
   # draw a rectangle around eyes
   for (ex,ey,ew,eh) in eyes:
      cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,255),2)


cv2.imshow('Identified Image', image)

cv2.waitKey(0)