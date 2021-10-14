import cv2
import numpy as np

# open cv tra ve gia tri cac kenh mau mac dinh la B G R
img = cv2.imread('images/thu.jpg')
# copy image
img_clone = img.copy()
# Lay kich thuoc cua anh, anh co 307200 pixels
# print(img_clone.size)
# print(type(img_clone))
# width= so cot, height= so hang, depth= so kenh mau
print(img_clone.shape)

# Lay ma tran theo tung kenh mau
B = img[:,:,0] 
G = img[:,:,1] 
R = img[:,:,2]

B = B*0.114
G = G*0.587
R = R*0.299
gray = B+G+R
imgGray = img.copy()
for i in range(3):
    imgGray[:,:,i] = gray

cv2.imshow('Image Gray', imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()

p1 = [50, 60]
p2 = [320, 320]
# toa do lan luot la 50,60 320,320
# Cut = imgGray[50:320, 60:320]
Cut = imgGray[p1[0]:p2[0], p1[1]:p2[1]]
cv2.imshow('Region of Interest', Cut)
cv2.waitKey(0)
cv2.destroyAllWindows()