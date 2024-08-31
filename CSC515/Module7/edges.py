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
background = np.ones(shape = (300, 500, 3), dtype = np.uint8)
cv2.rectangle(background, pt1 = (50, 50), pt2 = (150, 150), color = (0, 0, 227), thickness = cv2.FILLED)
circle = cv2.circle(background, center = (350, 200), radius = 50, color = (0, 128, 0), thickness = cv2.FILLED)
# https://stackoverflow.com/a/56186046/13801562
circle = (circle * 255).astype(np.uint8)

# Edge Detection
# https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html?ref=blog.roboflow.com
canny = cv2.Canny(circle, 10, 25)
# https://docs.opencv.org/4.x/d5/d0f/tutorial_py_gradients.html
sobel = cv2.Sobel(circle, ddepth = cv2.CV_8U, dx = 1, dy = 0, ksize = 7)
laplacian = cv2.Laplacian(circle, cv2.CV_8U)

# Measure of performance is amount of outline

# Add noise
# https://www.askpython.com/python/examples/adding-noise-images-opencv
def addGaussianNoise(image, mean = 0, std = 25):
    noise = np.random.normal(mean, std, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)
    return noisy_image

# Noisy version
noisyversion = addGaussianNoise(background)
cannyn = cv2.Canny(noisyversion, 110, 400)
sobeln = cv2.Sobel(noisyversion, ddepth = cv2.CV_8U, dx = 1, dy = 0, ksize = 7)
laplaciann = cv2.Laplacian(circle, cv2.CV_8U)

# cv2.imshow('Original Image', background)
# cv2.imshow('Canny', canny)
# cv2.imshow('Laplacian', cannyn)
# cv2.waitKey(0)

titles = ['Original', 'Canny', 'Sobel', 'Laplacian',
          'Gaussian Noise', 'Canny Noise', 'Sobel Noise', 'Laplacian Noise']

images = [background, canny, sobel, laplaciann,
          noisyversion, cannyn, sobeln, laplaciann]

for i in range(8):
    plt.subplot(2, 4, i + 1), plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
    plt.title(titles[i])
    plt.tight_layout()
plt.suptitle('Edge Detection Results', fontsize = 25).set_color('#171819')
plt.tight_layout()
plt.show()