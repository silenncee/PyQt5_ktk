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
        self.timer.timeout.connect(self.update_timer)
        self.time = QTime(0, 0, 0)
        self.current_test = 0  # 0: no test, 1: first test, 2: squats, 3: final test

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.timer_layout = QHBoxLayout()

        self.text_timer = QLabel("00:00")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: black")
        self.text_timer.setAlignment(Qt.AlignCenter)

        self.timer_layout.addWidget(self.text_timer)
        self.layout.addLayout(self.timer_layout)
        self.setLayout(self.layout)

    def update_timer(self):
        if self.current_test == 1:  # First test
            self.time = self.time.addSecs(-1)
            self.text_timer.setText(self.time.toString("mm:ss"))
            if self.time == QTime(0, 0):
                self.timer.stop()
                self.current_test = 0
                self.text_timer.setStyleSheet("color: black")
        elif self.current_test == 2:  # Squats test
            self.time = self.time.addSecs(-1)
            self.text_timer.setText(self.time.toString("mm:ss"))
            if self.time == QTime(0, 0):
                self.timer.stop()
                self.current_test = 0
                self.text_timer.setStyleSheet("color: black")
        elif self.current_test == 3:  # Final test
            self.time = self.time.addSecs(-1)
            if self.time >= QTime(0, 0, 45):
                self.text_timer.setStyleSheet("color: green")
            elif self.time >= QTime(0, 0, 15):
                self.text_timer.setStyleSheet("color: black")
            else:
                self.text_timer.setStyleSheet("color: red")
            self.text_timer.setText(self.time.toString("mm:ss"))
            if self.time == QTime(0, 0):
                self.timer.stop()
                self.current_test = 0
                self.text_timer.setStyleSheet("color: black")

    def start_timer1(self):
        self.current_test = 1
        self.time = QTime(0, 0, 15)
        self.text_timer.setStyleSheet("color: black")
        self.timer.start(1000)

    def start_timer2(self):
        self.current_test = 2
        self.time = QTime(0, 0, 45)
        self.text_timer.setStyleSheet("color: black")
        self.timer.start(1000)

    def start_timer3(self):
        self.current_test = 3
        self.time = QTime(0, 0, 59)
        self.text_timer.setStyleSheet("color: green")
        self.timer.start(1000)


class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Тест Руфье")
        self.resize(800, 600)
        self.move(100, 100)

        self.layout = QHBoxLayout()
        self.input_layout = QVBoxLayout()

        # FIO input
        self.fio_label = QLabel("Введите ФИО:")
        self.fio_input = QLineEdit()
        self.fio_input.setFixedWidth(200)
        self.input_layout.addWidget(self.fio_label)
        self.input_layout.addWidget(self.fio_input)

        # Age input
        self.age_label = QLabel("Введите полных лет:")
        self.age_input = QLineEdit()
        self.age_input.setFixedWidth(200)
        self.input_layout.addWidget(self.age_label)
        self.input_layout.addWidget(self.age_input)

        # First test
        self.info_text = QLabel(instr.text2)
        self.input_layout.addWidget(self.info_text)
        self.pulse1_input = QLineEdit()
        self.pulse1_input.setFixedWidth(200)
        self.pulse1_input.setPlaceholderText("Введите пульс")
        self.input_layout.addWidget(self.pulse1_input)

        self.test1_button = QPushButton("Начать первый тест")
        self.test1_button.setFixedWidth(200)
        self.test1_button.clicked.connect(self.start_test1)
        self.input_layout.addWidget(self.test1_button)

        # Squats test
        self.squats_text = QLabel(instr.text3)
        self.input_layout.addWidget(self.squats_text)
        self.start_squats_button = QPushButton("Начать делать приседания")
        self.start_squats_button.setFixedWidth(200)
        self.start_squats_button.clicked.connect(self.start_squats)
        self.input_layout.addWidget(self.start_squats_button)

        # Final test
        self.final_text = QLabel(instr.text4)
        self.input_layout.addWidget(self.final_text)
        self.final_button = QPushButton("Начать финальный тест")
        self.final_button.setFixedWidth(200)
        self.final_button.clicked.connect(self.start_final_test)
        self.input_layout.addWidget(self.final_button)

        self.pulse2_input = QLineEdit()
        self.pulse2_input.setFixedWidth(200)
        self.pulse2_input.setPlaceholderText("Пульс за первые 15 секунд")
        self.input_layout.addWidget(self.pulse2_input)

        self.pulse3_input = QLineEdit()
        self.pulse3_input.setFixedWidth(200)
        self.pulse3_input.setPlaceholderText("Пульс за последние 15 секунд")
        self.input_layout.addWidget(self.pulse3_input)

        # Submit button
        self.next_window_button = QPushButton("Отправить результаты")
        self.next_window_button.setFixedWidth(200)
        self.next_window_button.clicked.connect(self.open_third_window)
        self.input_layout.addWidget(self.next_window_button)

        # Add layouts
        self.test_widget = TestWin()
        self.layout.addLayout(self.input_layout)
        self.layout.addWidget(self.test_widget)
        self.setLayout(self.layout)

    def start_test1(self):
        self.test_widget.start_timer1()

    def start_squats(self):
        self.test_widget.start_timer2()

    def start_final_test(self):
        self.test_widget.start_timer3()

    def open_third_window(self):
        try:
            age = int(self.age_input.text())
            pulse1 = int(self.pulse1_input.text())
            pulse2 = int(self.pulse2_input.text())
            pulse3 = int(self.pulse3_input.text())
            
            if not self.fio_input.text():
                QMessageBox.warning(self, "Ошибка", "Введите ФИО")
                return
                
            self.final_window = FinalWin(age, pulse1, pulse2, pulse3)
            self.final_window.show()
            self.close()
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите корректные числовые значения")
