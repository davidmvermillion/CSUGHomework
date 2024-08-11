# Import packages
import cv2
from os import chdir
from os.path import abspath, dirname, join
import matplotlib.pyplot as plt

# Force script execution directory to current path
chdir(dirname(abspath(__file__)))

# Import image
image = cv2.imread('Mod4CT2.jpg')

# Laplacian with Gaussian Blur
# https://csuglobal.instructure.com/courses/96788/pages/4-dot-3-image-filtering-in-opencv?module_item_id=4939424
def LapGaus(item, kernel):
    blur = cv2.GaussianBlur(item, (kernel, kernel), 10)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_32F)
    return laplacian

# Laplacian
def Laplacian(item, kernel):
    gray = cv2.cvtColor(item, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_32F, ksize = kernel)
    return laplacian

# Gaussian
def Gaussian(item, kernel):
    blur = cv2.GaussianBlur(item, (kernel, kernel), 10)
    return blur

# Kernals to test
k3 = 3
k5 = 5
k7 = 7

# Tested algorithms. Maintaining default sigma (10) from class tutorial
l3 = Laplacian(image, k3)
l5 = Laplacian(image, k5)
l7 = Laplacian(image, k7)

g3 = Gaussian(image, k3)
g5 = Gaussian(image, k5)
g7 = Gaussian(image, k7)

lp3 = LapGaus(image, k3)
lp5 = LapGaus(image, k5)
lp7 = LapGaus(image, k7)

# 3x3 subplots. rows are kernels, columns are methods. Add overall x and y axis labels
# Continue by adding overall axis labels and title along with adding notes for each block of code

# Display results
fig, axs = plt.subplots(nrows = 3, ncols = 3)
axs[0, 0].imshow(cv2.cvtColor(l3, cv2.COLOR_BGR2RGB))
axs[0, 0].set_title('Laplacian\nk = 3')
axs[0, 1].imshow(cv2.cvtColor(g3, cv2.COLOR_BGR2RGB))
axs[0, 1].set_title('Gaussian\nk = 3')
axs[0, 2].imshow(cv2.cvtColor(lp3, cv2.COLOR_BGR2RGB))
axs[0, 2].set_title('Gaussian and Laplacian\nk = 3')

axs[1, 0].imshow(cv2.cvtColor(l5, cv2.COLOR_BGR2RGB))
axs[1, 0].set_title('Laplacian\nk = 5')
axs[1, 1].imshow(cv2.cvtColor(g5, cv2.COLOR_BGR2RGB))
axs[1, 1].set_title('Gaussian\nk = 5')
axs[1, 2].imshow(cv2.cvtColor(lp5, cv2.COLOR_BGR2RGB))
axs[1, 2].set_title('Gaussian and Laplacian\nk = 5')

axs[2, 0].imshow(cv2.cvtColor(l7, cv2.COLOR_BGR2RGB))
axs[2, 0].set_title('Laplacian\nk = 7')
axs[2, 1].imshow(cv2.cvtColor(g7, cv2.COLOR_BGR2RGB))
axs[2, 1].set_title('Gaussian\nk = 7')
axs[2, 2].imshow(cv2.cvtColor(lp7, cv2.COLOR_BGR2RGB))
axs[2, 2].set_title('Gaussian and Laplacian\nk = 7')

axs[0, 0].axis('off')
axs[0, 1].axis('off')
axs[0, 2].axis('off')
axs[1, 0].axis('off')
axs[1, 1].axis('off')
axs[1, 2].axis('off')
axs[2, 0].axis('off')
axs[2, 1].axis('off')
axs[2, 2].axis('off')

fig.tight_layout()
plt.show()