import numpy as np
import tensorflow as tf
import pandas as pd

# Đọc dữ liệu từ tệp CSV
data=pd.read_csv('Student_Performance.csv') # Thay 'du_lieu.csv' bằng đường dẫn tới tệp CSV của bạn
x = np.array(data.iloc[:, :5])  # Lấy dữ liệu từ 5 cột đầu tiên
y = np.array(data.iloc[:, 5])  # Lấy dữ liệu từ cột cuối cùng

# Chuẩn hóa dữ liệu
x = (x - np.mean(x, axis=0)) / np.std(x, axis=0)

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra (80% - 20%)
split_point = int(0.5 * len(data))
training_x, test_x = x[:split_point], x[split_point:]
training_y, test_y = y[:split_point], y[split_point:]

# Thiết lập mô hình TensorFlow
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(5,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Huấn luyện mô hình
model.fit(training_x, training_y, epochs=10, batch_size=32)

# Đánh giá mô hình trên tập kiểm tra
loss, accuracy = model.evaluate(test_x, test_y)
print("Độ chính xác trên tập kiểm tra:", accuracy)  