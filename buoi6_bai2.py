import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

# Hàm xử lý sự kiện khi nhấn nút "Hiển thị ảnh"
def show_image():
    angle = int(angle_entry.get())  # Lấy góc xoay từ trường nhập liệu
    image_path = image_path_entry.get()  # Lấy đường dẫn đến ảnh từ trường nhập liệu
    
    # Đọc ảnh từ đường dẫn
    image = cv2.imread(image_path)
    
    # Xoay ảnh
    rotated_image = rotate_image(image, angle)
    
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    # Ảnh đã xoay
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
    plt.title('Rotated Image')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

     # Kiểm tra xem ảnh có tồn tại hay không
        if image is None:
            error_label.config(text="Không thể đọc ảnh!", fg="red")
            return

     # Hiển thị ảnh gốc
        display_image(image, "Original Image")
        
    # Hiển thị ảnh bằng matplotlib
    '''plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title('Rotated Image')
    plt.show()'''

# Hàm xoay ảnh
def rotate_image(image, angle):
    height, width = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

# Tạo cửa sổ tkinter
root = tk.Tk()
root.title("Xoay Ảnh")

# Nhập góc xoay
angle_label = tk.Label(root, text="Góc Xoay (đơn vị: độ):")
angle_label.pack()
angle_entry = ttk.Entry(root)
angle_entry.pack()

# Nhập địa chỉ ảnh
image_path_label = tk.Label(root, text="Địa chỉ ảnh:")
image_path_label.pack()
image_path_entry = ttk.Entry(root)
image_path_entry.pack()

# Nút hiển thị ảnh
show_button = tk.Button(root, text="Hiển Thị Ảnh", command=show_image)
show_button.pack()

# Chạy vòng lặp chính của tkinter
root.mainloop()
