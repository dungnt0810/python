import cv2 as cv
import numpy as np
import scipy.signal as sig

# A1 = 3x3 matrix
A1 = np.array([[1,3, 1],
                    [0, -1, 1],
                    [2, 2, -1]])

# Template
kernel = np.array([[1,2],
                [0,-1]])

# kernel = np.array ([[8, 9, 10, 11, 12],
#                     [15, 16, 17, 18, 19],
#                     [22, 23, 24, 25, 26],
#                     [29, 30, 31, 32, 33]])

#dap an ơ tam 
#cross-correlation
print(sig.correlate2d(A1, kernel, boundary='fill', mode='same'))

#convolution
# print(sig.convolve(A1, kernel, mode='same'))

#median filter = lọc trung vị
# print(sig.medfilt(A1, kernel_size=None))