from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton
import instr
from third_window import ThirdWin


class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.setWindowTitle("Здоровье2")
        self.resize(400, 300)
        self.move(1000, 600)

        self.layout = QVBoxLayout()

        self.fio_label = QLabel("Введите ФИО:")
        self.layout.addWidget(self.fio_label)

        self.fio_input = QLineEdit()
        self.fio_input.setFixedWidth(200)
        self.layout.addWidget(self.fio_input)

        self.age_label = QLabel("Введите полных лет:")
        self.layout.addWidget(self.age_label)

        self.age_input = QLineEdit()
        self.age_input.setFixedWidth(200)
        self.layout.addWidget(self.age_input)

        self.info_text = QLabel(instr.text2)
        self.layout.addWidget(self.info_text)

        self.start_test_button = QPushButton("Начать первый тест")
        self.start_test_button.setFixedWidth(150)
        self.layout.addWidget(self.start_test_button)

        self.additional_input = QLineEdit()
        self.additional_input.setFixedWidth(200)
        self.layout.addWidget(self.additional_input)

        self.additional_text = QLabel(instr.text3)
        self.layout.addWidget(self.additional_text)

        self.start_squats_button = QPushButton("Начать делать приседания")
        self.start_squats_button.setFixedWidth(150)
        self.layout.addWidget(self.start_squats_button)

        self.squats_info_text = QLabel(instr.text4)
        self.layout.addWidget(self.squats_info_text)

        self.final_button = QPushButton("Начать финальный тест")
        self.final_button.setFixedWidth(150)
        self.layout.addWidget(self.final_button)


        self.next_window_button = QPushButton("Отправить результаты")
        self.next_window_button.setFixedWidth(150)
        self.next_window_button.clicked.connect(self.open_third_window)
        self.layout.addWidget(self.next_window_button)

        self.setLayout(self.layout)

    def open_third_window(self):
        self.third_window = ThirdWin()
        self.third_window.show()
        self.close()
