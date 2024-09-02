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
    # carplate_img = 0

    for x, y, w, h in carplate_rects:
        cv2.rectangle(carplate_overlay,
                      (x, y),
                      (x + w, y + h),
                      (255, 0, 0),
                      25) 
        
    # for x, y, w, h in carplate_rects:
    #     carplate_img = carplate_overlay[y + 15: y + h - 10,
    #                          x + 15: x + w - 20] 


    return carplate_overlay

# def PlateZoom(image):
#     carplate_overlay = cv2.cvtColor(image.copy(), cv2.COLOR_GRAY2BGR)
#     carplate_rects = rusPlateFinder.detectMultiScale(carplate_overlay,
#                                                      scaleFactor = 1.1,
#                                                      minNeighbors = 5)
#     for x, y, w, h in carplate_rects:
#         carplate_img = carplate_overlay[y + 15: y + h - 10,
#                              x + 15: x + w - 20]
#     return carplate_img

def carplate_extract(image):
    
    carplate_rects = rusPlateFinder.detectMultiScale(image,scaleFactor=1.1, minNeighbors=5) 
    carplate_rects_df = pd.DataFrame(carplate_rects)

    plates_x = np.min(carplate_rects_df[0])
    plates_y = min(carplate_rects_df[1])
    plates_h = min(carplate_rects_df[3])
    plates_w = min(carplate_rects_df[2])
    carplate_img = image[plates_y : plates_y + plates_h, plates_x : plates_x + plates_w]

    # for x,y,w,h in carplate_rects: 

        
    #     carplate_img = image[y+15:y+h-10,x+15:x+w-20] 
        
    #     return carplate_img
    return carplate_img

# # Come back to this idea later
# for i in range(len(source)):
#     plates[i] = CarplateDetect(gray[i])
#     plateszoom[i] = carplate_extract(gray[i])




# # Implement processing if required to make plates horizontal


# Figure out how to display results once confirmed that they work

# titles = ['Original', 'Canny', 'Sobel', 'Laplacian',
#           'Gaussian Noise', 'Canny Noise', 'Sobel Noise', 'Laplacian Noise']

images = [plates[0], plates[1], plates[2],
          plateszoom[0], plateszoom[1], plateszoom[2]]

# Convert BGR to RGB
# for i in range(len(plates)):
#     plates[i] = cv2.cvtColor(plates[i], cv2.COLOR_BGR2RGB)

for i in range(3):
    plt.subplot(3, 2, i + 1), plt.imshow(plates[i], 'gray')
    plt.xticks([]), plt.yticks([])
    # plt.title(titles[i])
    plt.tight_layout()
# plt.suptitle('Edge Detection Results', fontsize = 25).set_color('#171819')
plt.tight_layout()
plt.show()