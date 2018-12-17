# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwidow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from mylabel import Mylabel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/WindowsIcon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.label_paint = QtWidgets.QLabel(self.centralwidget)
        self.label_paint = Mylabel(self.centralwidget)
        self.label_paint.setGeometry(QtCore.QRect(10, 25, 551, 551))
        self.label_paint.setText("")
        self.label_paint.setObjectName("label_paint")
        self.pushButton_find_road = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_find_road.setGeometry(QtCore.QRect(630, 120, 111, 41))
        self.pushButton_find_road.setObjectName("pushButton_find_road")
        self.pushButton_clear_road = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear_road.setGeometry(QtCore.QRect(630, 180, 111, 41))
        self.pushButton_clear_road.setObjectName("pushButton_clear_road")
        self.pushButton_put_rabbit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_put_rabbit.setGeometry(QtCore.QRect(630, 240, 111, 41))
        self.pushButton_put_rabbit.setObjectName("pushButton_put_rabbit")
        self.pushButton_put_radish = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_put_radish.setGeometry(QtCore.QRect(630, 300, 111, 41))
        self.pushButton_put_radish.setObjectName("pushButton_put_radish")
        self.pushButton_load_map = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_load_map.setGeometry(QtCore.QRect(630, 420, 111, 41))
        self.pushButton_load_map.setObjectName("pushButton_load_map")
        self.pushButton_save_map = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save_map.setGeometry(QtCore.QRect(630, 480, 111, 41))
        self.pushButton_save_map.setObjectName("pushButton_save_map")
        self.pushButton_put_wall = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_put_wall.setGeometry(QtCore.QRect(630, 360, 111, 41))
        self.pushButton_put_wall.setObjectName("pushButton_put_wall")
        self.label_mapsize = QtWidgets.QLabel(self.centralwidget)
        self.label_mapsize.setGeometry(QtCore.QRect(590, 30, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_mapsize.setFont(font)
        self.label_mapsize.setObjectName("label_mapsize")

        self.spinBox_width= QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_width.setGeometry(QtCore.QRect(661, 30, 51, 31))
        self.spinBox_width.setObjectName("spinBox_width")
        self.spinBox_width.setValue(self.label_paint.map.width)
        self.spinBox_width.setMinimum(1)
        self.spinBox_height = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_height.setGeometry(QtCore.QRect(721, 30, 51, 31))
        self.spinBox_height.setObjectName("spinBox_height")
        self.spinBox_height.setValue(self.label_paint.map.height)
        self.spinBox_height.setMinimum(1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "兔子抓萝卜"))
        self.pushButton_find_road.setText(_translate("MainWindow", "寻找路径"))
        self.pushButton_clear_road.setText(_translate("MainWindow", "清除路径"))
        self.pushButton_put_rabbit.setText(_translate("MainWindow", "放置兔子"))
        self.pushButton_put_radish.setText(_translate("MainWindow", "放置萝卜"))
        self.pushButton_load_map.setText(_translate("MainWindow", "载入地图"))
        self.pushButton_save_map.setText(_translate("MainWindow", "保存地图"))
        self.pushButton_put_wall.setText(_translate("MainWindow", "放置墙壁"))
        self.label_mapsize.setText(_translate("MainWindow", "地图大小"))


