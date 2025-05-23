from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# Текстовые сообщения для вывода
txt_index = "Ваш индекс Руфье: "
txt_workheart = "Работоспособность сердца: "
txt_nodata = '''
нет данных для такого возраста'''
txt_res = [
    '''низкая.
Срочно обратитесь к врачу!''',
    '''удовлетворительная.
Обратитесь к врачу!''',
    '''средняя.
Возможно, стоит дополнительно обследоваться у врача.''',
    '''выше среднего''',
    '''высокая'''
]

class FinalWin(QWidget):
    def __init__(self, age_input, pulse1, pulse2, pulse3):
        super().__init__()
        self.age = int(age_input)
        self.pulse1 = int(pulse1)
        self.pulse2 = int(pulse2)
        self.pulse3 = int(pulse3)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Результаты теста Руфье")
        self.resize(600, 400)
        self.move(200, 200)

        self.ruf_index = self.calculate_ruf_index()

        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Результаты теста Руфье")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Index
        index_label = QLabel(f"{txt_index} {self.ruf_index:.2f}")
        index_label.setFont(QFont("Arial", 14))
        index_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(index_label)

        # Heart work capacity
        if self.age < 7:
            result_message = txt_nodata
        else:
            level = self.neud_level(self.age)
            result_index = self.ruffier_result(self.ruf_index, level)
            result_message = txt_res[result_index]

        heart_label = QLabel(f"{txt_workheart} {result_message}")
        heart_label.setFont(QFont("Arial", 12))
        heart_label.setAlignment(Qt.AlignCenter)
        heart_label.setWordWrap(True)
        layout.addWidget(heart_label)

        # Close button
        close_button = QPushButton("Закрыть")
        close_button.setFixedWidth(200)
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def calculate_ruf_index(self):
        return (self.pulse1 + self.pulse2 + self.pulse3 - 200) / 10

    def neud_level(self, age):
        if age < 7:
            return float('inf')
        norm_age = (min(age, 15) - 7) // 2
        result = 21 - norm_age * 1.5
        return result

    def ruffier_result(self, r_index, level):
        if r_index >= level:
            return 0
        level -= 4
        if r_index >= level:
            return 1
        level -= 5
        if r_index >= level:
            return 2
        level -= 5.5
        if r_index >= level:
            return 3
        return 4

    def close_window(self):
        self.close()
