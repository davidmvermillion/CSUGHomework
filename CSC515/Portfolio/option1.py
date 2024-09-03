# Import packages
import cv2;
from os import chdir
from os.path import abspath, dirname
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Force script execution directory to current path
chdir(dirname(abspath(__file__)))

# Read images
image1 = cv2.imread('Images/Image6.jpg') # Russian Taxi at Angle and Some Distance
image2 = cv2.imread('Images/Image7.jpg') # Two Russian Plates with Telephoto Lens
image3 = cv2.imread('Images/Image4.jpg') # Ontario Plate
source = list([image1, image2, image3])
# https://www.geeksforgeeks.org/how-to-fix-valueerror-setting-an-array-element-with-a-sequence/
source = np.array(source, dtype = list)

# Define placeholders
gray = np.array([0, 1, 2], dtype = list)
plates = np.array(list(range(3)), dtype = list)
plateszoom = np.array(list(range(3)), dtype = list)

# Convert to Grayscale
for i in range(len(source)):
    gray[i] = cv2.cvtColor(source[i], cv2.COLOR_BGR2GRAY)

# # Load Classifier
rusPlateReader = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_license_plate_rus_16stages.xml')
rusPlateFinder = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

# Detect Plates
# https://github.com/kennethleungty/Car-Plate-Detection-OpenCV-TesseractOCR/blob/main/Car%20Plate%20Detection%20with%20OpenCV%20and%20TesseractOCR.ipynb
def CarplateDetect(image):
    # Color rectangle overlay on grayscale image plate detection area
    carplate_overlay = cv2.cvtColor(image.copy(), cv2.COLOR_GRAY2BGR)
    carplate_rects = rusPlateFinder.detectMultiScale(carplate_overlay,
                                                     scaleFactor = 1.1,
                                                     minNeighbors = 5) 

    for x, y, w, h in carplate_rects:
        cv2.rectangle(carplate_overlay,
                      (x, y),
                      (x + w, y + h),
                      (255, 0, 0),
                      25) 

    return carplate_overlay

def PlateZoom(image):
    carplate_overlay = cv2.cvtColor(image.copy(), cv2.COLOR_GRAY2BGR)
    carplate_rects = rusPlateFinder.detectMultiScale(carplate_overlay,
                                                     scaleFactor = 1.1,
                                                     minNeighbors = 5)
    if len(carplate_rects) < 2:
        for x, y, w, h in carplate_rects:
            carplate_img = carplate_overlay[y + 15: y + h - 10,
                                x + 15: x + w - 20]
    else:
        exit
    return carplate_img

def SemiZoom(image, overlay):
    image = overlay[image[1]:image[1]+image[3],
                    image[0]:image[0]+image[2]]
    return image

# First Image Extracted
plates_0 = CarplateDetect(gray[0])
plateszoom_0 = PlateZoom(gray[0])

# Second Image Extracted
# Lots of room to improve code here
carplate_rects = rusPlateFinder.detectMultiScale(gray[1],
                                                     scaleFactor = 1.1,
                                                     minNeighbors = 5)
carplate_overlay = cv2.cvtColor(gray[1].copy(), cv2.COLOR_GRAY2BGR)
carplate_rects_0 = carplate_rects[0]
carplate_rects_1 = carplate_rects[1]
plates_1 = CarplateDetect(gray[1])
plateszoom_1 = SemiZoom(carplate_rects_0, carplate_overlay)
plateszoom_2 = SemiZoom(carplate_rects_1, carplate_overlay)

# Third Image
# Non-Russian plate not identified and therefore not extracted
plates_2 = CarplateDetect(gray[2])




# # Implement processing if required to make plates horizontal


# Figure out how to display results once confirmed that they work

# titles = ['Original', 'Canny', 'Sobel', 'Laplacian',
#           'Gaussian Noise', 'Canny Noise', 'Sobel Noise', 'Laplacian Noise']

images = [plates_0, plates_1, plates_2,
          plateszoom_0, plateszoom_1, plateszoom_2]

# Convert BGR to RGB
# for i in range(len(plates)):
#     plates[i] = cv2.cvtColor(plates[i], cv2.COLOR_BGR2RGB)

for i in range(6):
    plt.subplot(3, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
    # plt.title(titles[i])
    plt.tight_layout()
# plt.suptitle('Edge Detection Results', fontsize = 25).set_color('#171819')
plt.tight_layout()
plt.show()