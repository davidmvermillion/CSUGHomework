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

# Display results
fig, axs = plt.subplots(nrows = 3, ncols = 3)
fig.suptitle('Smaller Kernel High-Pass Filters\nRetain More Detail', fontsize = 25).set_color('#171819')

# Kernel size 3
axs[0, 0].imshow(cv2.cvtColor(l3, cv2.COLOR_BGR2RGB))
axs[0, 1].imshow(cv2.cvtColor(g3, cv2.COLOR_BGR2RGB))
axs[0, 2].imshow(cv2.cvtColor(lp3, cv2.COLOR_BGR2RGB))

# Kernel size 5
axs[1, 0].imshow(cv2.cvtColor(l5, cv2.COLOR_BGR2RGB))
axs[1, 1].imshow(cv2.cvtColor(g5, cv2.COLOR_BGR2RGB))
axs[1, 2].imshow(cv2.cvtColor(lp5, cv2.COLOR_BGR2RGB))

# Kernel size 7
axs[2, 0].imshow(cv2.cvtColor(l7, cv2.COLOR_BGR2RGB))
axs[2, 1].imshow(cv2.cvtColor(g7, cv2.COLOR_BGR2RGB))
axs[2, 2].imshow(cv2.cvtColor(lp7, cv2.COLOR_BGR2RGB))

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

# Set global axes
fig.supxlabel('Method', horizontalalignment = 'left', x = 0.19).set_color('#707070')
fig.supylabel('Kernel Size', rotation = 'horizontal', verticalalignment = 'bottom', y = 0.1).set_color('#707070')
fig.text(0.31, 0.07, 'Laplacian', ha = 'center', va = 'center').set_color('#606060')
fig.text(0.58, 0.07, 'Gaussian', ha = 'center', va = 'center').set_color('#606060')
fig.text(0.85, 0.07, 'Gaussian & Laplacian', ha = 'center', va = 'center').set_color('#606060')
fig.text(0.17, 0.2, '7', ha = 'center', va = 'center').set_color('#606060')
fig.text(0.17, 0.43, '5', ha = 'center', va = 'center').set_color('#606060')
fig.text(0.17, 0.67, '3', ha = 'center', va = 'center').set_color('#606060')

# Show results
fig.tight_layout()
plt.show()