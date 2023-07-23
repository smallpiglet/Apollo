from PyQt6.QtWidgets import QApplication
from Lib.MainWindow import MainWindow
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()