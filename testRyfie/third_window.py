from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

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
    def __init__(self, age_input, additional_input, fin_input, fin2_input):
        super().__init__()
        self.age = int(age_input)
        self.additional_input = int(additional_input)
        self.fin_input = int(fin_input)
        self.fin2_input = int(fin2_input)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Индекс Руфье")
        self.resize(400, 200)


        self.ruf_index = self.calculate_ruf_index()


        if self.age < 7:
            result_message = txt_nodata
        else:
            level = self.neud_level(self.age)
            result_index = self.ruffier_result(self.ruf_index, level)
            result_message = txt_res[result_index]

        layout = QVBoxLayout()
        message = QLabel(f"{txt_index} {self.ruf_index:.2f}")
        heart_message = QLabel(f"{txt_workheart} {result_message}")
        layout.addWidget(message)
        layout.addWidget(heart_message)
        layout.setAlignment(message, Qt.AlignCenter)
        layout.setAlignment(heart_message, Qt.AlignCenter)

        self.setLayout(layout)

    def calculate_ruf_index(self):
        return (self.fin_input + self.fin2_input + self.additional_input - 200) / 10

    def neud_level(self, age):
        if age < 7:
            return float('inf')  # Возраст менее 7 лет, уровень "неуд" не применим
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
