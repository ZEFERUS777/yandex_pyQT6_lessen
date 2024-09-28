from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLCDNumber
import sys


class MiniCalculator(QWidget):
    def __init__(self):
        super(MiniCalculator, self).__init__()
        self.main_layout = QHBoxLayout(self)
        self.tex1_layout = QVBoxLayout(self)
        self.tex2_layout = QVBoxLayout(self)
        self.btn_conv = QVBoxLayout(self)
        self.lcd_display_layout = QVBoxLayout(self)

        self.label_1 = QLabel('Первое число(целое):', self)
        self.number_1 = QLineEdit(self)

        self.label_2 = QLabel('Второе число(целое):', self)
        self.number_2 = QLineEdit(self)
        self.tex1_layout.addWidget(self.label_1)
        self.tex1_layout.addWidget(self.number_1)
        self.tex1_layout.addWidget(self.label_2)
        self.tex1_layout.addWidget(self.number_2)

        self.calculate_button = QPushButton('->', self)
        self.calculate_button.clicked.connect(self.calculate)
        self.btn_conv.addWidget(self.calculate_button)

        self.lbl_t2_1 = QLabel('Сумма:', self)
        self.lbl_t2_2 = QLabel('Разность:', self)
        self.lbl_t2_3 = QLabel('Произведение:', self)
        self.lbl_t2_4 = QLabel('Частное:', self)

        self.tex2_layout.addWidget(self.lbl_t2_1)
        self.tex2_layout.addWidget(self.lbl_t2_2)
        self.tex2_layout.addWidget(self.lbl_t2_3)
        self.tex2_layout.addWidget(self.lbl_t2_4)

        self.result_sum = QLCDNumber(self)
        self.result_sub = QLCDNumber(self)
        self.result_mul = QLCDNumber(self)
        self.result_div = QLCDNumber(self)

        self.lcd_display_layout.addWidget(self.result_sum)
        self.lcd_display_layout.addWidget(self.result_sub)
        self.lcd_display_layout.addWidget(self.result_mul)
        self.lcd_display_layout.addWidget(self.result_div)

        self.main_layout.addLayout(self.tex1_layout)
        self.main_layout.addLayout(self.btn_conv)
        self.main_layout.addLayout(self.tex2_layout)
        self.main_layout.addLayout(self.lcd_display_layout)

    def calculate(self):
        try:
            num1 = int(self.number_1.text())
            num2 = int(self.number_2.text())

            # Вычисляем результаты
            self.result_sum.display(num1 + num2)
            self.result_sub.display(num1 - num2)
            self.result_mul.display(num1 * num2)

            # Обрабатываем деление на 0
            if num2 == 0:
                self.result_div.display("Error")
            else:
                self.result_div.display(f"{num1 / num2:.3f}")

        except ValueError:
            self.result_sum.display("Error")
            self.result_sub.display("Error")
            self.result_mul.display("Error")
            self.result_div.display("Error")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = MiniCalculator()
    calculator.show()
    sys.exit(app.exec())
