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

# Hàm xử lý sự kiện khi nút "Save Image" được nhấn
def save_image():
    global img
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG Image", "*.jpg"), ("PNG Image", "*.png")])
    if file_path:
        cv2.imwrite(file_path, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

# Hàm xử lý sự kiện khi nút "Apply Blur" được nhấn
def apply_blur():
    global img
    blurred_img = cv2.GaussianBlur(img, (21, 21), 0)  # Áp dụng bộ lọc Gaussian Blur
    display_image(blurred_img, 'Blurred Image')

# Hàm xử lý sự kiện khi nút "Draw" được nhấn
def draw_on_image():
    global img
    drawing = False
    last_x, last_y = 0, 0

    def draw(event):
        nonlocal drawing, last_x, last_y
        if drawing:
            x, y = event.x, event.y
            cv2.line(img, (last_x, last_y), (x, y), (0, 255, 0), 5)
            last_x, last_y = x, y
            display_image(img, 'Drawing on Image')

    def start_draw(event):
        nonlocal drawing, last_x, last_y
        drawing = True
        last_x, last_y = event.x, event.y

    def stop_draw(event):
        nonlocal drawing
        drawing = False

    label.bind("<B1-Motion>", draw)  # Xử lý sự kiện vẽ khi chuột di chuyển
    label.bind("<Button-1>", start_draw)  # Xử lý sự kiện bắt đầu vẽ khi nhấn chuột trái
    label.bind("<ButtonRelease-1>", stop_draw)  # Xử lý sự kiện kết thúc vẽ khi thả chuột trái
# Hàm xử lý sự kiện khi nút "Convert to Grayscale" được nhấn
def convert_to_grayscale():
    global img
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # Chuyển đổi sang ảnh xám
    display_image(gray_img, 'Grayscale Image')

# Hàm hiển thị hình ảnh trong cửa sổ
def display_image(image, window_title='Image'):
    image = Image.fromarray(image)
    photo = ImageTk.PhotoImage(image=image)
    label.config(image=photo)
    label.image = photo
    root.title(window_title)

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Image Processing App")

# Tạo nút để mở hình ảnh
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)

# Tạo nút để lưu hình ảnh
save_button = tk.Button(root, text="Save Image", command=save_image)
save_button.pack(pady=10)

# Tạo nút để áp dụng bộ lọc làm mờ
blur_button = tk.Button(root, text="Apply Blur", command=apply_blur)
blur_button.pack(pady=10)

# Tạo nút để vẽ lên hình ảnh
draw_button = tk.Button(root, text="Draw", command=draw_on_image)
draw_button.pack(pady=10)

# Label để hiển thị hình ảnh
label = tk.Label(root)
label.pack()

# Khởi tạo biến img và original_img
img = None
original_img = None

# Chạy vòng lặp chính của Tkinter
root.mainloop()
