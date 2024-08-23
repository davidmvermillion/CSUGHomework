# Import packages
import cv2
from os import chdir
import numpy as np
from os.path import abspath, dirname
import matplotlib.pyplot as plt

# Force script execution directory to current path
chdir(dirname(abspath(__file__)))

# Import images
image_dtol = cv2.imread('Dark-Light.png')
image_ltod = cv2.imread('Light-Dark.png')
image_dtol = cv2.cvtColor(image_dtol, cv2.COLOR_BGR2GRAY)
image_ltod = cv2.cvtColor(image_ltod, cv2.COLOR_BGR2GRAY)

# Settings
# Dark to Light Adaptive Thresholding
dtolth1 = cv2.adaptiveThreshold(image_dtol, 10, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 1111, 2)
dtolth2 = cv2.adaptiveThreshold(image_dtol, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 1111, 2)

# Light to Dark Adaptive Thresholding
ltodth1 = cv2.adaptiveThreshold(image_ltod, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
ltodth2 = cv2.adaptiveThreshold(image_ltod, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

titles = ['Dark to Light\nGrayscale', 'Light to Dark\nGrayscale',
          'Dark to Light\nMean', 'Dark to Light\nGaussian',
          'Light to Dark\nMean', 'Light to Dark\nGaussian']

images = [image_dtol, image_ltod, dtolth1, dtolth2, ltodth1, ltodth2]

for i in range(6):
    plt.subplot(3, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
    plt.title(titles[i])
    plt.tight_layout()
plt.suptitle('Adaptive Thresholding for Opposite Lighting', fontsize = 20).set_color('#171819')
plt.tight_layout()
plt.show()