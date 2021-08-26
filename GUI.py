from PyQt5.Qt import QWidget, QCheckBox
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QSplitter
from PaintBoard import PaintBoard
import numpy as np
import tensorflow.keras as keras

class MainWidget(QWidget):
    def __init__(self):
        super().__init__(None)
        self.__paintBoard = PaintBoard()
        self.__Initscreen()

    def __Initscreen(self):
        self.setFixedSize(640, 480)
        self.setWindowTitle("手写数字识别")

        main_layout = QHBoxLayout(self)
        main_layout.setSpacing(10)

        main_layout.addWidget(self.__paintBoard)

        sub_layout = QVBoxLayout()
        sub_layout.setContentsMargins(5, 5, 5, 5)

        splitter = QSplitter(self)
        sub_layout.addWidget(splitter)

        self.__label = QLabel(self)
        sub_layout.addWidget(self.__label)

        self.__btn_recognize = QPushButton("开始识别")
        self.__btn_recognize.setParent(self)
        self.__btn_recognize.clicked.connect(self.on_recognize_clicked)
        sub_layout.addWidget(self.__btn_recognize)

        self.__btn_clear = QPushButton("清空画板")
        self.__btn_clear.setParent(self)
        self.__btn_clear.clicked.connect(self.__paintBoard.clear)
        sub_layout.addWidget(self.__btn_clear)

        self.__btn_quit = QPushButton("退出")
        self.__btn_quit.setParent(self)
        self.__btn_quit.clicked.connect(exit)
        sub_layout.addWidget(self.__btn_quit)

        self.__cbtn_eraser = QCheckBox("  使用橡皮擦")
        self.__cbtn_eraser.setParent(self)
        self.__cbtn_eraser.clicked.connect(self.on_eraser_clicked)
        sub_layout.addWidget(self.__cbtn_eraser)

        main_layout.addLayout(sub_layout)

    def on_recognize_clicked(self):
        image = self.__paintBoard.getImage()
        image.save("test.png")
        img = keras.preprocessing.image.load_img("test.png", target_size=(28, 28))
        img = img.convert('L')
        x = keras.preprocessing.image.img_to_array(img)
        x = abs(255 - x)
        x = np.expand_dims(x, axis=0)
        x = x / 255.0
        model = keras.models.load_model('model.h5')
        prediction = model.predict(x)
        output = np.argmax(prediction, axis=1)
        self.__label.setText('识别为：'+str(output[0]))

    def on_eraser_clicked(self):
        if self.__cbtn_eraser.isChecked():
            self.__paintBoard.EraserMode = True
        else:
            self.__paintBoard.EraserMode = False
