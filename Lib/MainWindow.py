from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QTextEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.text = QTextEdit(self)