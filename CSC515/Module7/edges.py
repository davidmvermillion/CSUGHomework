# Import packages
import cv2
from os import chdir
from os.path import abspath, dirname
import matplotlib.pyplot as plt
import numpy as np

# Force script execution directory to current path
chdir(dirname(abspath(__file__)))

# Create Square and Circle in Background
# https://medium.com/jungletronics/opencv-image-basics-2e63d973851a
background = np.ones(shape = (300, 500, 3))
cv2.rectangle(background, pt1 = (50, 50), pt2 = (150, 150), color = (0, 0, 227), thickness = cv2.FILLED)
cv2.circle(background, center = (350, 200), radius = 50, color = (0, 128, 0), thickness = cv2.FILLED)

# plt.imshow(square)
cv2.imshow('Original Image', background)
cv2.waitKey(0)

# titles = ['Dark to Light\nGrayscale', 'Light to Dark\nGrayscale',
#           'Dark to Light\nMean', 'Dark to Light\nGaussian',
#           'Light to Dark\nMean', 'Light to Dark\nGaussian']

# images = [image_dtol, image_ltod, dtolth1, dtolth2, ltodth1, ltodth2]

# for i in range(6):
#     plt.subplot(3, 2, i + 1), plt.imshow(images[i], 'gray')
#     plt.xticks([]), plt.yticks([])
#     plt.title(titles[i])
#     plt.tight_layout()
# plt.suptitle('Adaptive Thresholding for Opposite Lighting', fontsize = 20).set_color('#171819')
# plt.tight_layout()
# plt.show()