from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QApplication, QWidget, QVBoxLayout
import instr
from second_window import SecondWin

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def set_appear(self):
        self.setWindowTitle("Здоровье")
        self.resize(400, 300)
        self.move(1000, 600)

    def initui(self):
        self.hello_text = QLabel(instr.text_hello)
        self.instruction = QLabel(instr.txt_instruction)
        self.button = QPushButton("Начать")

        self.button.setFixedWidth(150)
        self.button.clicked.connect(self.open_second_window)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button)
        self.layout.setAlignment(self.button, Qt.AlignCenter)

        self.setLayout(self.layout)

    def open_second_window(self):
        self.second_win = SecondWin()
        self.second_win.show()
        self.hide()

app = QApplication([])
main_win = MainWin()
main_win.set_appear()
main_win.show()
app.exec_()


