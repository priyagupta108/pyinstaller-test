import sys

from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = QWidget()
    example.setGeometry(100, 100, 640, 480)
    example.show()
    print('App loaded')
    sys.exit(app.exec_())
