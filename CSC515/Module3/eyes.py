# Import packages
import cv2
from os import chdir
from os.path import abspath, dirname, join

# Force script execution directory to current path
# https://stackoverflow.com/a/69556612/13801562
chdir(dirname(abspath(__file__)))

# https://stackoverflow.com/a/59717885/13801562
# https://www.tutorialspoint.com/how-to-detect-eyes-in-an-image-using-opencv-python

# read input image
img = cv2.imread('DMV.png')

# convert to grayscale of each frames
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# read the haarcascade to detect the faces in an image
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# read the haarcascade to detect the eyes in an image
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye_tree_eyeglasses.xml')

# detects faces in the input image
faces = face_cascade.detectMultiScale(gray, 1.3, 4)
print('Number of detected faces:', len(faces))

# loop over the detected faces
for (x,y,w,h) in faces:
   roi_gray = gray[y:y+h, x:x+w]
   roi_color = img[y:y+h, x:x+w]
   
   # detects eyes of within the detected face area (roi)
   eyes = eye_cascade.detectMultiScale(roi_gray)
   
   # draw a rectangle around eyes
   for (ex,ey,ew,eh) in eyes:
      cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,255),2)

# display the image with detected eyes
cv2.imshow('Eyes Detection',img)
cv2.waitKey(0)
cv2.destroyAllWindows()