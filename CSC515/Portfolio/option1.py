# Import packages
import cv2;
from os import chdir
from os.path import abspath, dirname
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import easyocr as eor

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
# Non-Russian plate (Canadian) not identified by algorithm and therefore not extracted
plates_2 = CarplateDetect(gray[2])

# Read Plates in Extracted Images
# https://medium.com/@draj0718/text-recognition-and-extraction-in-images-93d71a337fc8


# Rotation Processing
# https://medium.com/@maritaganta/how-to-properly-rotate-an-image-with-opencv-475e44a252f6
# Functions
def calculate_slope(point1, point2):
    # Calculate the slope between two points
    delta_y = point2[1] - point1[1]
    delta_x = point2[0] - point1[0]
    
    # Avoid division by zero
    if delta_x != 0:
        slope = delta_y / delta_x
    else:
        slope = np.inf
    
    return slope

def calculate_rotation_angle(point1, point2):
    # Calculate the angle between the line connecting the two points and the horizontal axis
    delta_y = point2[1] - point1[1]
    delta_x = point2[0] - point1[0]
    
    # Calculate the angle using arctan
    angle = np.arctan(delta_y, delta_x)
    
    return angle

def rotate_image(image, angle, center):
    # Get the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    
    # Perform the rotation
    rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
    
    return rotated_image

def RotationProcess(image, point1, point2):
    slope = calculate_slope(point1, point2)
    angle = np.arctan(slope)
    angle = np.degrees(angle)
    center = (image.shape[1] // 2, image.shape[0] // 2)
    rotated_image = rotate_image(image, angle, center)
    return rotated_image

# Rotate Plates
# Points come from examining original zoomed images for points near bottom corners of plates to align bottom horizontal axes
rotated_plate_0 = RotationProcess(plateszoom_0, (30, 156), (441, 195))
rotated_plate_1 = RotationProcess(plateszoom_1, (10.2, 74.3), (234.7, 71.2))
rotated_plate_2 = RotationProcess(plateszoom_2, (10, 75), (234, 72))

# Additional Processing steps
# Function from Module 4 assignment
def Gaussian(item, kernel):
    blur = cv2.GaussianBlur(item, (kernel, kernel), 10)
    return blur

# EasyOCR hint from: https://medium.com/@draj0718/text-recognition-and-extraction-in-images-93d71a337fc8
reader = eor.Reader(['ru'])

# First plate needs blurring to read correctly
# Some extraneous characters read
rotated_plate_0_g = Gaussian(rotated_plate_0, 5)
result_0 = reader.readtext(rotated_plate_0_g, paragraph = 'False')
result_frame_0 = pd.DataFrame(result_0)

# Second plate reads fine without additional processing. Gaussian added to remove slash.
rotated_plate_1_g = Gaussian(rotated_plate_1, 5)
result_1 = reader.readtext(rotated_plate_1, paragraph = 'False')
result_frame_1 = pd.DataFrame(result_1)

# Third plate requires additional work to read correctly.
# Gaussian at 3 reads all but the first character and k=5 misreads the last two characters.
rotated_plate_2_g = Gaussian(rotated_plate_2, 3)
result_2 = reader.readtext(rotated_plate_2_g, paragraph = 'False')
result_frame_2 = pd.DataFrame(result_2)


# titles = ['Original', 'Canny', 'Sobel', 'Laplacian',
#           'Gaussian Noise', 'Canny Noise', 'Sobel Noise', 'Laplacian Noise']

images = [plates_0, plates_1, plates_2,
          rotated_plate_0, rotated_plate_1, rotated_plate_2]

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