from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
import time

from map import Map


class Mylabel(QLabel):
    def __init__(self, QWidget):
        super(Mylabel, self).__init__()

        # the init map is 8*8
        self.setFixedSize(550,550)
        self.grid_len = min(550/8, 550/8)
        self.map = Map(8,8)
        self.map.load_map("file_test.txt")

    def paintEvent(self, a0: QPaintEvent):
        self.paint_line()
        self.paint_wall()
        self.paint_rabbit()
        self.paint_radish()
        self.paint_path()

    def paint_line(self):
        painter = QPainter(self)
        pen = QPen()
        pen.setColor(QColor(0,0,0))
        painter.setPen(pen)

        for i in range(self.map.width+1):
            painter.drawLine(i*self.grid_len, 0, i*self.grid_len, self.map.height*self.grid_len)
        for j in range(self.map.height+1):
            painter.drawLine(0, j*self.grid_len, self.map.width*self.grid_len, j*self.grid_len)

        painter.end()

    def paint_wall(self):
        painter = QPainter(self)
        brush = QBrush()
        brush.setStyle(Qt.Dense4Pattern)
        brush.setColor(QColor(185,149,119))
        painter.setBrush(brush)
        for i in range(len(self.map.wall)):
            pos = self.map.wall[i]
            painter.drawRect(QRect(pos.x()*self.grid_len, pos.y()*self.grid_len,
                                   self.grid_len, self.grid_len))
        painter.end()

    def paint_rabbit(self):
        painter = QPainter(self)

        rabbit_img = QImage("imgs/rabbit.jpg")
        pos = self.map.rabbit
        # 为了不遮挡边框，这里需要加上和减去1像素的长度
        target = QRect(pos.x()*self.grid_len+1, pos.y()*self.grid_len+1,
                                   self.grid_len-1, self.grid_len-1)
        source = QRect(0,0,500,500)
        painter.drawImage(target, rabbit_img, source)
        painter.end()

    def paint_radish(self):
        painter = QPainter(self)

        radish_img = QImage("imgs/WindowsIcon.jpg")
        pos = self.map.radish
        target = QRect(pos.x()*self.grid_len+1, pos.y()*self.grid_len+1,
                                   self.grid_len-1, self.grid_len-1)
        source = QRect(0,0,500,500)
        painter.drawImage(target, radish_img, source)
        painter.end()

    def paint_path(self):
        painter = QPainter(self)
        brush = QBrush()
        brush.setStyle(Qt.Dense4Pattern)
        brush.setColor(QColor(244,60,91))
        painter.setBrush(brush)

        # 原先是从终点找寻到起点，现在为了直观，改成从起点到终点
        self.map.path.reverse()
        for i in range(len(self.map.path)-2):
            pos = self.map.path[i+1]
            painter.drawRect(QRect(pos.x()*self.grid_len, pos.y()*self.grid_len,
                                   self.grid_len, self.grid_len))
        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Mylabel()
    dlg.map.a_star_searching()
    dlg.show()
    sys.exit(app.exec_())