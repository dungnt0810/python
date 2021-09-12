import cv2

# đọc file ảnh
img = cv2.imread('images/thu.jpg')
print(img)

# Lấy kích thước của ảnh
(h, w, d) = img.shape
print("width={}, height={}, depth={}".format(w, h, d))

# show file ảnh 
cv2.imshow('image', img)
# nhấn phím bất kì để thoát cửa sổ
cv2.waitKey(0)
cv2.destroyAllWindows()

