from PyQt5.QtWidgets import *
import sys


class Test(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        btn = QPushButton('关闭', self)

        btn.clicked.connect(self.close)
        btn.clicked()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Test()
    dlg.show()
    sys.exit(app.exec_())