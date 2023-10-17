import cv2
a1= cv2.imread('a.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('anh ban dau ',a1)
cv2.imwrite('anh_den_trang.png',a1)