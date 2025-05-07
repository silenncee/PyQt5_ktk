from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton
import instr
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
from third_window import ThirdWin

time = QTime(0, 0, 15)
# time.addSecs(-1)
# time.toString("hh:mm:ss")

class TestWin(QWidget):
    def timer1event(self):

        global time
    # time = QTime(0, 1, 0)
        time = time.AddSecs(-1)
        self.timer = QTimer()
        self.timer.timeout.connect(self.self.timer1event)
        self.timer.start(1000)
        self.timer.stop()
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()


    def connects(self):
        self.bth_test1.clicked.connect(self.timer_test)
        self.bth_test1.clicked.connect(self.timer_test)



class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.setWindowTitle("Результат")
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

        self.bth_test1 = QPushButton("Начать первый тест")
        self.bth_test1.setFixedWidth(150)
        self.layout.addWidget(self.bth_test1)

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

