import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread('test.png')
# Hiển thị ảnh gốc
        plt.subplot(1, 2, 1)
        plt.title("Original")
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.axis('off')

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Normalize the grayscale image
normalized_gray_img = cv2.normalize(gray_img, None, 0, 255, cv2.NORM_MINMAX)

# Display the original image
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Display the normalized image
plt.subplot(1, 2, 2)
plt.title("Normalized")
plt.imshow(normalized_gray_img, cmap='gray')
plt.axis('off')

plt.show()
