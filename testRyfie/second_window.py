from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
from third_window import FinalWin
import instr


class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.timer = QTimer()
        self.timer1 = QTimer()
        self.timer2 = QTimer()
        self.time = QTime(0, 0, 0)  # Начальное время

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.timer_layout = QHBoxLayout()

        self.text_timer = QLabel("00:00:15")
        self.text_timer.setFont(QFont("Times", 20, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")

        self.timer_layout.addStretch()
        self.timer_layout.addWidget(self.text_timer, alignment=Qt.AlignRight)

        self.layout.addLayout(self.timer_layout)




        self.setLayout(self.layout)

    def start_timer1(self):
        self.time = QTime(0, 0, 15)
        self.timer.timeout.connect(self.timer1_event)
        self.timer.start(1000)
        self.timer1_event()

    def timer1_event(self):
        self.time = self.time.addSecs(-1)
        self.text_timer.setText(self.time.toString("mm:ss"))

        if self.time == QTime(0, 0):

            self.timer.stop()



    def start_timer2(self):
        self.time = QTime(0, 0, 45)
        self.timer1.timeout.connect(self.timer2_event)
        self.timer1.start(1000)
        self.timer2_event()

    def timer2_event(self):
        self.time = self.time.addSecs(-1)
        self.text_timer.setText(self.time.toString("mm:ss"))
        if self.time == QTime(0, 0):
            self.timer1.stop()


    def start_timer3(self):
        self.time = QTime(0, 0, 59)
        self.timer2.timeout.connect(self.timer3_event)
        self.timer2.start(1000)
        self.timer3_event()

    def timer3_event(self):
        self.time = self.time.addSecs(-1)
        if self.time >= QTime(0, 0, 45):
            self.text_timer.setStyleSheet("color: green")
        elif self.time >= QTime(0, 0, 15):
            self.text_timer.setStyleSheet("color: black")
        else:
            self.text_timer.setStyleSheet("color: red")

        self.text_timer.setText(self.time.toString("mm:ss"))
        if self.time == QTime(0, 0):
            self.timer2.stop()


class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Результат")
        self.resize(800, 400)
        self.move(1000, 600)

        self.layout = QHBoxLayout()
        self.input_layout = QVBoxLayout()

        self.fio_label = QLabel("Введите ФИО:")
        self.input_layout.addWidget(self.fio_label)

        self.fio_input = QLineEdit()
        self.fio_input.setFixedWidth(200)
        self.input_layout.addWidget(self.fio_input)

        self.age_label = QLabel("Введите полных лет:")
        self.input_layout.addWidget(self.age_label)

        self.age_input = QLineEdit()  #возраст инпут
        self.age_input.setFixedWidth(200)
        self.input_layout.addWidget(self.age_input)

        self.info_text = QLabel(instr.text2)
        self.input_layout.addWidget(self.info_text)

        self.additional_input = QLineEdit()
        self.additional_input.setFixedWidth(200)
        self.input_layout.addWidget(self.additional_input)             #инпут. пульс1

        self.additional_text = QLabel(instr.text3)
        self.input_layout.addWidget(self.additional_text)

        self.test1_button = QPushButton("Начать первый тест")
        self.test1_button.setFixedWidth(150)
        self.test1_button.clicked.connect(self.start_test1)
        self.input_layout.addWidget(self.test1_button)

        self.start_squats_button = QPushButton("Начать делать приседания")
        self.start_squats_button.setFixedWidth(150)
        self.start_squats_button.clicked.connect(self.start_squats)
        self.input_layout.addWidget(self.start_squats_button)

        self.squats_info_text = QLabel(instr.text4)
        self.input_layout.addWidget(self.squats_info_text)

        self.final_button = QPushButton("Начать финальный тест")
        self.final_button.setFixedWidth(150)
        self.final_button.clicked.connect(self.start_final_test)
        self.input_layout.addWidget(self.final_button)

        self.fin_input = QLineEdit()
        self.fin_input.setFixedWidth(200)                #инпуты
        self.input_layout.addWidget(self.fin_input)

        self.fin2_input = QLineEdit()
        self.fin2_input.setFixedWidth(200)
        self.input_layout.addWidget(self.fin2_input)

        self.next_window_button = QPushButton("Отправить результаты")
        self.next_window_button.setFixedWidth(150)
        self.next_window_button.clicked.connect(self.open_third_window)
        self.input_layout.addWidget(self.next_window_button)

        # Правая часть для TestWin
        self.test_widget = TestWin()
        self.layout.addLayout(self.input_layout)  # Добавляем ввод данных
        self.layout.addWidget(self.test_widget)  # Добавляем TestWin

        self.setLayout(self.layout)

    def start_test1(self):
        self.test_widget.start_timer1()

    def start_squats(self):
        self.test_widget.start_timer2()  # Запускаем таймер приседаний

    def start_final_test(self):
        self.test_widget.start_timer3()


    def open_third_window(self):
        age_value = self.age_input.text()
        additional_value = self.additional_input.text()
        fin_value = self.fin_input.text()
        fin2_value = self.fin2_input.text()

        # Создаем экземпляр FinalWin и передаем значения
        self.final_window = FinalWin(age_value, additional_value, fin_value, fin2_value)
        self.final_window.show()  # Показываем окно с индексом Руфье

        self.close()  # Закрываем текущее окно
