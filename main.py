import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.resize(1200, 800)
    w.move(400, 100)
    w.setWindowTitle('MipsAssembler & Dissembler')
    w.show()

    sys.exit(app.exec_())