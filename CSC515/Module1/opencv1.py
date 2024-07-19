# Import packages
import cv2
from os import chdir
from os.path import abspath, dirname, join

# Force script execution directory to current path
# https://stackoverflow.com/a/69556612/13801562
chdir(dirname(abspath(__file__)))

# Import image (renamed from downloaded name of 'shutterstock93075775--250.jpg' to be more descriptive)
image = cv2.imread('brain.jpg')

# Put image in desktop folder. This path is machine-specific and is not portable.
# I don't like putting things on the desktop. I also don't like writing this as an absolute path.
# https://stackoverflow.com/a/41587740/13801562
newimagepath = '/Users/davidmvermillion/Desktop/PlzNoMoreDesktop'
cv2.imwrite(join(newimagepath, 'brain.jpg'), image)

# Show image and name window
cv2.imshow('Brain Image', image)

# https://www.geeksforgeeks.org/python-opencv-cv2-imshow-method/
# This step is required to prevent auto-closing/crashing upon run. Output can be exited by pressing any key.
cv2.waitKey(0)