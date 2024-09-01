# Import packages
import cv2
from os import chdir
from os.path import abspath, dirname
import matplotlib.pyplot as plt
import numpy as np

# Force script execution directory to current path
chdir(dirname(abspath(__file__)))

# Read images
image1 = cv2.imread('Images/Image2.jpg') # RUS License Plate w/ Shadow
image2 = cv2.imread('Images/Image3.jpg') # Clear RUS License Plate Lighting
image3 = cv2.imread('Images/Image5.jpg') # Two European Plates w/ Flat Lighting
source = list([image1, image2, image3])
# https://www.geeksforgeeks.org/how-to-fix-valueerror-setting-an-array-element-with-a-sequence/
source = np.array(source, dtype = list)

# Define placeholders
gray = np.array([0, 1, 2], dtype = list)
plates = np.array(list(range(3)), dtype = list)

# Convert to Grayscale
for i in range(len(source)):
    gray[i] = cv2.cvtColor(source[i], cv2.COLOR_BGR2GRAY)

# # Load Classifier
rusPlateFinder16 = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_license_plate_rus_16stages.xml')
rusPlateReader = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

# Detect Plates
for i in range(len(gray)):
    plates[i] = rusPlateFinder16.detectMultiScale(
        gray[i],
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (40, 40)
    )

# # Implement processing if required to make plates horizontal

# # Boundary Boxes around Detected Plates

# for (x, y, w, h) in plates:
#    roi_gray = gray[y: y + h, x: x + w]
#    roi_color = source[y: y + h, x: x + w]
   
#    # Detect Plates and name after the philosopher
#    plato = rusPlateReader.detectMultiScale(roi_gray)
   
#    # Create coordinates and parameters
#    plato_x = min(plato[:, 0])
#    plato_y = min(plato[:, 1])
#    plato_h = max(plato[:, 3])
#    plato_w = max(plato[:, 0]) + max(plato[:, 2]) - min(plato[:, 0])

#    # Create rectangle around detected plates
#    cv2.rectangle(
#       roi_color,
#       (plato_x, plato_y),
#       (plato_x + plato_w, plato_y + plato_h),
#       (0, 0, 255),
#       8
#    )

# Figure out how to display results once confirmed that they work

# titles = ['Original', 'Canny', 'Sobel', 'Laplacian',
#           'Gaussian Noise', 'Canny Noise', 'Sobel Noise', 'Laplacian Noise']

# images = [background, canny, sobel, laplaciann,
#           noisyversion, cannyn, sobeln, laplaciann]

# Convert BGR to RGB
# cv2.cvtColor(source, cv2.COLOR_BGR2RGB)

# for i in range(3):
#     plt.subplot(3, 1, i + 1), plt.imshow(gray[i], 'gray')
#     plt.xticks([]), plt.yticks([])
#     # plt.title(titles[i])
#     plt.tight_layout()
# # plt.suptitle('Edge Detection Results', fontsize = 25).set_color('#171819')
# plt.tight_layout()
# plt.show()