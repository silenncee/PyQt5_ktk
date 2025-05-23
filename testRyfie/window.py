from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QFont
import instr
from second_window import TestWin, SecondWin
# from second_window import FinalWin

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def set_appear(self):
        self.setWindowTitle("Тест Руфье")
        self.resize(800, 600)
        self.move(100, 100)

    def init_ui(self):
        self.hello_text = QLabel(instr.text_hello)
        self.hello_text.setFont(QFont("Arial", 16, QFont.Bold))
        self.hello_text.setAlignment(Qt.AlignCenter)
        
        self.instruction = QLabel(instr.txt_instruction)
        self.instruction.setFont(QFont("Arial", 12))
        self.instruction.setWordWrap(True)
        self.instruction.setAlignment(Qt.AlignCenter)
        
        self.button = QPushButton("Начать")
        self.button.setFont(QFont("Arial", 12))
        self.button.setFixedWidth(200)
        self.button.clicked.connect(self.open_second_window)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.layout.setSpacing(20)
        self.layout.setContentsMargins(50, 50, 50, 50)

        self.setLayout(self.layout)

    def open_second_window(self):
        self.second_win = SecondWin()
        self.testwin = TestWin()
        # self.finalwin = FinalWin()

        self.second_win.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication([])
    main_win = MainWin()
    main_win.set_appear()
    main_win.show()
    app.exec_()

