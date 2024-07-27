# Import packages
import cv2
from os import chdir
from os.path import abspath, dirname, join

# Force script execution directory to current path
# https://stackoverflow.com/a/69556612/13801562
chdir(dirname(abspath(__file__)))

# Import puppy image
image = cv2.imread('shutterstock215592034--250.jpg')

# Split channels
blue = image[:, :, 0]
green = image[:, :, 1]
red = image[:, :, 2]

# Recombine channels
recombined = cv2.merge((blue, green, red))
flipped = cv2.merge((blue, red, green))

# Show results
cv2.imshow('Original Image', image)
cv2.imshow('Blue Channel, Grayscale', blue)
cv2.imshow('Red Channel, Grayscale', red)
cv2.imshow('Green Channel, Grayscale', green)
cv2.imshow('Recombined Image', recombined)
cv2.imshow('Red and Green Channels Flipped', flipped)

cv2.waitKey(0)