import sys
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QFileDialog, QApplication
from PyQt5.QtCore import QPoint
import mainwidow

"""
@author:wxz
"""

class MyWindow(QMainWindow, mainwidow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        self.put_rabbit_isclicked = False
        self.put_radish_isclicked = False
        self.put_wall_isclicked = False

        # 添加信号槽
        self.pushButton_clear_road.clicked.connect(self.pushButton_clear_road_clicked)
        self.pushButton_find_road.clicked.connect(self.pushButton_find_road_clicked)
        self.pushButton_put_rabbit.clicked.connect(self.pushButton_put_rabbit_clicked)
        self.pushButton_put_radish.clicked.connect(self.pushButton_put_radish_clicked)
        self.pushButton_put_wall.clicked.connect(self.pushButton_put_wall_clicked)
        self.pushButton_load_map.clicked.connect(self.pushButton_load_map_clicked)
        self.pushButton_save_map.clicked.connect(self.pushButton_save_map_clicked)
        self.spinBox_width.valueChanged.connect(self.spinBox_width_changed)
        self.spinBox_height.valueChanged.connect(self.spinBox_height_changed)

    def pushButton_find_road_clicked(self):
        result = self.label_paint.map.a_star_searching()
        if result[0]:
            time = result[1]
            self.label_paint.update()
            QMessageBox.information(self, "Time", "A*查找时间为"+str('%.3f' % time+"s"))
        else:
            QMessageBox.information(self, "提示", "无路径")

    def pushButton_clear_road_clicked(self):
        self.label_paint.map.path.clear()
        self.label_paint.update()

    def pushButton_put_rabbit_clicked(self):
        self.put_rabbit_isclicked = not self.put_rabbit_isclicked
        # 开启放兔子按钮时，其余两个按钮应该禁用了
        self.put_wall_isclicked = False
        self.pushButton_put_wall.setStyleSheet("color: black")
        self.put_radish_isclicked = False
        self.pushButton_put_radish.setStyleSheet("color: black")

        if self.put_rabbit_isclicked:
            self.pushButton_put_rabbit.setStyleSheet("color: blue")
        else:
            self.pushButton_put_rabbit.setStyleSheet("color: black")

    def pushButton_put_radish_clicked(self):
        self.put_radish_isclicked = not self.put_radish_isclicked
        self.put_rabbit_isclicked = False
        self.pushButton_put_rabbit.setStyleSheet("color: black")
        self.put_wall_isclicked = False
        self.pushButton_put_wall.setStyleSheet("color: black")

        if self.put_radish_isclicked:
            self.pushButton_put_radish.setStyleSheet("color: blue")
        else:
            self.pushButton_put_radish.setStyleSheet("color: black")

    def pushButton_put_wall_clicked(self):
        self.put_wall_isclicked = not self.put_wall_isclicked
        self.put_rabbit_isclicked = False
        self.pushButton_put_rabbit.setStyleSheet("color: black")
        self.put_radish_isclicked = False
        self.pushButton_put_radish.setStyleSheet("color: black")

        if self.put_wall_isclicked:
            self.pushButton_put_wall.setStyleSheet("color: blue")
        else:
            self.pushButton_put_wall.setStyleSheet("color: black")

    def pushButton_load_map_clicked(self):
        file_path = QFileDialog.getOpenFileName(self, "选择地图", ".", "地图文件(*.txt)")
        if len(file_path[0]) == 0:
            QMessageBox.warning(self, "提示", "未选择文件")
        else:
            # 默认输入的地图是正确的
            self.label_paint.map.load_map(file_path[0])
            temp_map = self.label_paint.map
            self.label_paint.grid_len = min(550/temp_map.width, 550/temp_map.height)
            self.label_paint.map.load_map(file_path[0])
            self.label_paint.update()

    def pushButton_save_map_clicked(self):
        file_path = QFileDialog.getSaveFileName(self, "选择保存路径", ".", "地图文件(*.txt)")
        if len(file_path[0]) == 0:
            QMessageBox.warning(self, "提示", "未选择路径")
        else:
            self.label_paint.map.save_map(file_path[0])
            QMessageBox.information(self, "提示", "保存成功")


    def spinBox_width_changed(self):
        self.label_paint.map.width = self.spinBox_width.value()
        self.label_paint.map.rabbit = QPoint(-1, -1)
        self.label_paint.map.radish = QPoint(-1, -1)
        self.label_paint.map.wall.clear()
        self.label_paint.grid_len = min(550/self.label_paint.map.width,
                                        550/self.label_paint.map.height)
        self.label_paint.update()

    def spinBox_height_changed(self):
        self.label_paint.map.height = self.spinBox_height.value()
        self.label_paint.map.rabbit = QPoint(-1, -1)
        self.label_paint.map.radish = QPoint(-1, -1)
        self.label_paint.map.wall.clear()
        self.label_paint.grid_len = min(550/self.label_paint.map.width,
                                        550/self.label_paint.map.height)
        self.label_paint.update()


    def mousePressEvent(self, a0: QMouseEvent):

        x = (a0.x()-self.label_paint.pos().x())/self.label_paint.grid_len
        y = (a0.y()-self.label_paint.pos().y())/self.label_paint.grid_len
        position = QPoint(x, y)

        if 0 < x < self.label_paint.map.width and 0 < y < self.label_paint.map.height:
            if self.put_rabbit_isclicked:
                if not self.label_paint.map.on_special_object("wall", position):
                    if not self.label_paint.map.on_special_object("radish", position):
                        self.label_paint.map.set_rabbit(position)

            if self.put_radish_isclicked:
                if not self.label_paint.map.on_special_object("wall", position):
                    if not self.label_paint.map.on_special_object("rabbit", position):
                        self.label_paint.map.set_radish(position)

            if self.put_wall_isclicked:
                if not self.label_paint.map.on_special_object("rabbit", position):
                    if not self.label_paint.map.on_special_object("radish", position):
                        if not self.label_paint.map.on_special_object("wall", position):
                            self.label_paint.map.set_wall(position)
                        else:
                            index = self.label_paint.map.wall.index(position)
                            self.label_paint.map.wall.pop(index)
        self.label_paint.update()







if __name__ == "__main__":

    a = QApplication(sys.argv)
    t = MyWindow()
    t.show()
    sys.exit(a.exec_())
