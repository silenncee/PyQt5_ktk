from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

class ThirdWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.setWindowTitle("Третье окно")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        message = QLabel("Индекс Руфье:4.8")
        layout.addWidget(message)
        layout.setAlignment(message, Qt.AlignCenter)  
        self.setLayout(layout)

    def close_window(self):
        self.close()
