from PyQt5.QtWidgets import QWidget
from PyQt5.Qt import QPixmap, QPainter, QPoint, QPen, QColor, QSize
from PyQt5.QtCore import Qt

class PaintBoard(QWidget):
    def __init__(self):
        super().__init__(None)

        self.__size = QSize(480, 480)
        self.__board = QPixmap(self.__size)
        self.__board.fill(Qt.white)

        self.EraserMode = False
        self.__lastPos = QPoint(0, 0)
        self.__currentPos = QPoint(0, 0)
        self.__painter = QPainter()

        self.setFixedSize(self.__size)

    def paintEvent(self, paintEvent):
        self.__painter.begin(self)
        self.__painter.drawPixmap(0, 0, self.__board)
        self.__painter.end()

    def mousePressEvent(self, mouseEvent):
        # 鼠标按下时，获取鼠标的当前位置保存为上一次位置
        self.__currentPos = mouseEvent.pos()
        self.__lastPos = self.__currentPos

    def mouseMoveEvent(self, mouseEvent):
        # 鼠标移动时，更新当前位置，并在上一个位置和当前位置间画线
        self.__currentPos = mouseEvent.pos()
        self.__painter.begin(self.__board)

        if self.EraserMode == False:
            self.__painter.setPen(QPen(QColor("black"), 25))
        else:
            self.__painter.setPen(QPen(Qt.white, 40))

        self.__painter.drawLine(self.__lastPos, self.__currentPos)
        self.__painter.end()
        self.__lastPos = self.__currentPos
        self.update()

    def clear(self):
        self.__board.fill(Qt.white)
        self.update()

    def getImage(self):
        return self.__board.toImage()
