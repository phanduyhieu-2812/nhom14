import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


# Hàm xử lý sự kiện khi nút "Open Image" được nhấn
def open_image():
    global img, original_img
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    original_img = img.copy()
    display_image(img)


# Hàm xử lý sự kiện khi nút "Apply Filters" được nhấn
def apply_filters():
    global img
    kernel_sharpen_1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    kernel_sharpen_2 = np.array([[1, 1, 1], [1, -7, 1], [1, 1, 1]])
    kernel_sharpen_3 = np.array([[-1, -1, -1, -1, -1],
                                 [-1, 2, 2, 2, -1],
                                 [-1, 2, 8, 2, -1],
                                 [-1, 2, 2, 2, -1],
                                 [-1, -1, -1, -1, -1]]) / 8.0

    output_1 = cv2.filter2D(img, -1, kernel_sharpen_1)
    output_2 = cv2.filter2D(img, -1, kernel_sharpen_2)
    output_3 = cv2.filter2D(img, -1, kernel_sharpen_3)

    display_image(output_1, 'Sharpening')
    display_image(output_2, 'Excessive Sharpening')
    display_image(output_3, 'Edge Enhancement')
# Hàm xử lý sự kiện khi nút "Save Image" được nhấn
def save_image():
    global img
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG Image", "*.jpg"), ("PNG Image", "*.png")])
    if file_path:
        cv2.imwrite(file_path, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))


# Hàm xử lý sự kiện khi nút "Undo" được nhấn
def undo_filters():
    global img
    img = original_img.copy()
    display_image(img)


# Hàm hiển thị hình ảnh trong cửa sổ
def display_image(image, window_title='Image'):
    image = Image.fromarray(image)
    photo = ImageTk.PhotoImage(image=image)
    label.config(image=photo)
    label.image = photo
    root.title(window_title)


# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Image Filters")

# Tạo nút để mở hình ảnh
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)

# Tạo nút để áp dụng bộ lọc
apply_button = tk.Button(root, text="Apply Filters", command=apply_filters)
apply_button.pack(pady=10)
# Tạo nút để lưu hình ảnh
save_button = tk.Button(root, text="Save Image", command=save_image)
save_button.pack(pady=10)


# Tạo nút để hoàn tác bộ lọc
undo_button = tk.Button(root, text="Undo Filters", command=undo_filters)
undo_button.pack(pady=10)

# Label để hiển thị hình ảnh
label = tk.Label(root)
label.pack()

# Khởi tạo biến img và original_img
img = None
original_img = None

# Chạy vòng lặp chính của Tkinter
root.mainloop()
