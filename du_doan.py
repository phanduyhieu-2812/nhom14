import numpy as np
import tensorflow as tf

# Đọc dữ liệu từ file
data = np.loadtxt('Student_Performance.csv', delimiter=',', skiprows=1)

# Chia dữ liệu thành features (đặc trưng) và labels (nhãn)
features = data[:, :-1]
labels = data[:, -1]

# Chuẩn hóa dữ liệu
features = (features - np.mean(features, axis=0)) / np.std(features, axis=0)

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
train_ratio = 0.3
train_size = int(train_ratio * len(data))

train_features = features[:train_size]
train_labels = labels[:train_size]
test_features = features[train_size:]
test_labels = labels[train_size:]

# Xây dựng mô hình neural network
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(5,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile mô hình
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Huấn luyện mô hình
model.fit(train_features, train_labels, epochs=10, batch_size=32, verbose=1)

# Đánh giá mô hình trên tập kiểm tra
loss, accuracy = model.evaluate(test_features, test_labels, verbose=0)
print('Accuracy:', accuracy)