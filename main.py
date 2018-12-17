import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import mainwidow


class MyWindow(QMainWindow, mainwidow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_clear_road.clicked.connect(self.close)
        self.pushButton_find_road.clicked.connect(self.showMsg)

    def showMsg(self):
        QMessageBox.information(self, "dfj", "fe ")



if __name__ == "__main__":

    a = QApplication(sys.argv)
    t = MyWindow()
    t.show()
    sys.exit(a.exec_())
