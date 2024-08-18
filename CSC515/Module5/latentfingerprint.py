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
# Binary
(thresh, binary_img) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
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

# Display results
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