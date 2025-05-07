from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

class ThirdWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.setWindowTitle("Результат")
        self.resize(400, 300)
        self.move(1000, 600)

        layout = QVBoxLayout()

        message = QLabel("Индекс Руфье:4.8")
        layout.addWidget(message)
        layout.setAlignment(message, Qt.AlignCenter)  
        self.setLayout(layout)

    def close_window(self):
        self.close()
