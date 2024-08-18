# Import packages
import cv2
from os import chdir
import numpy as np
from os.path import abspath, dirname, join
import matplotlib.pyplot as plt

# Force script execution directory to current path
chdir(dirname(abspath(__file__)))

# Import image
# Source: https://www.pickpik.com/dirt-dirty-fingerprints-forensics-glass-grease-123528
image = cv2.imread('fingerprint.jpg')

# Settings
kernel = np.ones((3, 3), np.uint8)

# Try various individual operations
# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Global Binary
(thresh, binary_img) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
# Adaptive Binary
binary_img2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Grayscale Morphological Operations
# Erosion
erosion = cv2.erode(gray, kernel, iterations = 1)
erosion2 = cv2.erode(gray, kernel, iterations = 2)
# Dilation
dilation = cv2.dilate(gray, kernel, iterations = 1)
dilation2 = cv2.dilate(gray, kernel, iterations = 2)
# Open
opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
# Close
closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

# Binary Morphological Operations
# Erosion
erosionb = cv2.erode(binary_img2, kernel, iterations = 1)
erosion2b = cv2.erode(binary_img2, kernel, iterations = 2)
# Dilation
dilationb = cv2.dilate(binary_img2, kernel, iterations = 1)
dilation2b = cv2.dilate(binary_img2, kernel, iterations = 2)
# Open
openingb = cv2.morphologyEx(binary_img2, cv2.MORPH_OPEN, kernel)
# Close
closingb = cv2.morphologyEx(binary_img2, cv2.MORPH_CLOSE, kernel)

# Display differing effects of grayscale and binary sources for morphological transformations
# Source: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
images = [erosionb, dilationb, openingb, closingb,
          erosion, dilation, opening, closing]
titles = ['Binary\nErosion', 'Binary\nDilation', 'Binary\nOpening', 'Binary\nClosing',
          'Grayscale\nErosion', 'Grayscale\nDilation', 'Grayscale\nOpening', 'Grayscale\nClosing']
for i in range(8):
    plt.subplot(2, 4, i + 1), plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
    plt.title(titles[i])
    plt.tight_layout()
plt.suptitle('Binary Morphology on Top\nGrayscale Morphology on Bottom', fontsize = 25).set_color('#171819')
plt.tight_layout()
plt.show()

# Display overall results for comparison
fig, axs = plt.subplots(nrows = 3, ncols = 3)
fig.suptitle('Latent Fingerprint Morpholigical\nOperations had Varying Effects', fontsize = 25).set_color('#171819')

# Images
axs[0, 0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0, 1].imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
axs[0, 2].imshow(cv2.cvtColor(binary_img, cv2.COLOR_BGR2RGB))
axs[1, 0].imshow(cv2.cvtColor(opening, cv2.COLOR_BGR2RGB))
axs[1, 1].imshow(cv2.cvtColor(erosion, cv2.COLOR_BGR2RGB))
axs[1, 2].imshow(cv2.cvtColor(dilation, cv2.COLOR_BGR2RGB))
axs[2, 0].imshow(cv2.cvtColor(closing, cv2.COLOR_BGR2RGB))
axs[2, 1].imshow(cv2.cvtColor(erosion2, cv2.COLOR_BGR2RGB))
axs[2, 2].imshow(cv2.cvtColor(dilation2, cv2.COLOR_BGR2RGB))

# Titles
axs[0, 0].set_title('Original')
axs[0, 1].set_title('Grayscale')
axs[0, 2].set_title('Binary')
axs[1, 0].set_title('Opening')
axs[1, 1].set_title('Erosion')
axs[1, 2].set_title('Dilation')
axs[2, 0].set_title('Closing')
axs[2, 1].set_title('Erosion x2')
axs[2, 2].set_title('Dilation x2')

# Turn off individual image axes
axs[0, 0].axis('off')
axs[0, 1].axis('off')
axs[0, 2].axis('off')
axs[1, 0].axis('off')
axs[1, 1].axis('off')
axs[1, 2].axis('off')
axs[2, 0].axis('off')
axs[2, 1].axis('off')
axs[2, 2].axis('off')

# Show results
fig.tight_layout()
plt.show()