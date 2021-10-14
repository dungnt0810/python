import cv2
import numpy as np
from matplotlib import pyplot as plt
from numpy.core.fromnumeric import size

# open cv tra ve gia tri cac kenh mau mac dinh la B G R
img = cv2.imread('images/thu.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
im = img.copy()

cv2.imshow('image',im)

# histr = cv2.calcHist([im],[0],None,[256],[0,256])
# plt.plot(histr)
# plt.show()
# plt.close()

# ret, th1 = cv2.threshold(im, 80, 120, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)

# cv2.imshow('th1',th1)
cv2.imshow('th',th2)

kernel = np.ones((3,3))
binImg = th2/255
sizeSrc = th2.shape
sizeKernel = kernel.shape
# Them padding
R = sizeSrc[0] + sizeKernel[0] - 1
C = sizeSrc[1] + sizeKernel[1] - 1

N = np.zeros((R, C))
for i in range(sizeSrc[0]):
    for j in range(sizeSrc[1]):
        N[i+1, j+1] = binImg[i, j]
# # Dilation
for i in range(sizeSrc[0]):
    for j in range(sizeSrc[1]):
        k = N[i:i+sizeKernel[0], j:j+sizeKernel[1]]
        result = (k == kernel)
        final = np.all(result == True)
        if final: 
            binImg[i,j] = 1
        else:
            binImg[i,j] = 0

# Erosion
# for i in range(sizeSrc[0]):
#     for j in range(sizeSrc[1]):
#         k = N[i:i+sizeKernel[0], j:j+sizeKernel[1]]
#         result = (k == kernel)
#         final = np.any(result == True)
#         if final: 
#             binImg[i,j] = 1
#         else:
#             binImg[i,j] = 0

cv2.imshow('Morphological', binImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
