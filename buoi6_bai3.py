import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc hình ảnh
img = cv2.imread('test.png')

# Chuyển đổi và hiển thị ảnh gốc và ảnh grayscale đã chuẩn hóa
def show_images(img, processed_img):
    # Hiển thị ảnh gốc
    plt.subplot(1, 3, 1)
    plt.title("Original")
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    # Hiển thị ảnh grayscale chuẩn hóa
    plt.subplot(1, 3, 2)
    plt.title("Normalized Grayscale")
    plt.imshow(processed_img, cmap='gray')
    plt.axis('off')

    # Hiển thị ảnh xử lý
    plt.subplot(1, 3, 3)
    plt.title("Processed Image")
    plt.imshow(cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    # Hiển thị ảnh
    plt.show()

# Chuyển đổi thành ảnh grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Chuẩn hóa ảnh grayscale
normalized_gray_img = cv2.normalize(gray_img, None, 0, 255, cv2.NORM_MINMAX)

# Bộ lọc hình ảnh: Lọc lạnh
cold_filter = cv2.applyColorMap(normalized_gray_img, cv2.COLORMAP_WINTER)

# Bộ lọc hình ảnh: Lọc ấm
warm_filter = cv2.applyColorMap(normalized_gray_img, cv2.COLORMAP_HOT)

# Bộ lọc hình ảnh: Lọc làm mờ
blurred_img = cv2.GaussianBlur(img, (21, 21), 0)

# Hiển thị ảnh gốc và ảnh grayscale đã chuẩn hóa
show_images(img, normalized_gray_img)

# Hiển thị ảnh với các bộ lọc
show_images(cold_filter, cold_filter)
show_images(warm_filter, warm_filter)
show_images(blurred_img, blurred_img)
