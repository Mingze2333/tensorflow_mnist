from Decode import Decode
import numpy as np
import tensorflow as tf

class Data:
    # 训练集文件
    train_images_idx3_ubyte_file = 'MNIST_data/train-images.idx3-ubyte'
    # 训练集标签文件
    train_labels_idx1_ubyte_file = 'MNIST_data/train-labels.idx1-ubyte'
    # 测试集文件
    test_images_idx3_ubyte_file = 'MNIST_data/t10k-images.idx3-ubyte'
    # 测试集标签文件
    test_labels_idx1_ubyte_file = 'MNIST_data/t10k-labels.idx1-ubyte'

    # 数据载入
    @classmethod
    def load_train_images(cls, images=train_images_idx3_ubyte_file):
        return Decode.idx3_ubyte(images)

    @classmethod
    def load_train_labels(cls, labels=train_labels_idx1_ubyte_file):
        return Decode.idx1_ubyte(labels)

    @classmethod
    def load_test_images(cls, images=test_images_idx3_ubyte_file):
        return Decode.idx3_ubyte(images)

    @classmethod
    def load_test_labels(cls, labels=test_labels_idx1_ubyte_file):
        return Decode.idx1_ubyte(labels)

    # 数据处理
    @classmethod
    def standard(cls, images):
        images = images.astype('float32')
        images = images / 255
        return images

    @classmethod
    def one_hot(cls, labels):
        result = np.zeros((labels.shape[0], 10))
        for i in range(labels.shape[0]):
            result[i][int(labels[i])] = 1
        return result

class Network:
    # 初始化神经网络
    def __init__(self):
        self.x_train, self.x_test = Data.standard(Data.load_train_images()), Data.standard(Data.load_test_images())
        self.y_train, self.y_test = Data.one_hot(Data.load_train_labels()), Data.one_hot(Data.load_test_labels())
        self.model = tf.keras.Sequential()
        self.model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
        self.model.add(tf.keras.layers.Dense(256, activation='sigmoid'))
        self.model.add(tf.keras.layers.Dense(256, activation='sigmoid'))
        self.model.add(tf.keras.layers.Dense(10, activation='softmax'))
        self.model.summary()
        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])

    # 训练方法
    def train(self):
        self.model.fit(self.x_train, self.y_train, epochs=10, validation_data=(self.x_test, self.y_test))
        self.model.save('model.h5')
