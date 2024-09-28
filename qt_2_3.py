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
        self.btn_conv.addWidget(self.calculate_button)

        self.lbl_t2_1 = QLabel('Сумма:', self)
        self.lbl_t2_2 = QLabel('Разность:', self)
        self.lbl_t2_3 = QLabel('Произведение:', self)
        self.lbl_t2_4 = QLabel('Частное:', self)

        self.tex2_layout.addWidget(self.lbl_t2_1)
        self.tex2_layout.addWidget(self.lbl_t2_2)
        self.tex2_layout.addWidget(self.lbl_t2_3)
        self.tex2_layout.addWidget(self.lbl_t2_4)

        self.lcd_display_1 = QLCDNumber(self)
        self.lcd_display_2 = QLCDNumber(self)
        self.lcd_display_3 = QLCDNumber(self)
        self.lcd_display_4 = QLCDNumber(self)

        self.lcd_display_layout.addWidget(self.lcd_display_1)
        self.lcd_display_layout.addWidget(self.lcd_display_2)
        self.lcd_display_layout.addWidget(self.lcd_display_3)
        self.lcd_display_layout.addWidget(self.lcd_display_4)

        self.main_layout.addLayout(self.tex1_layout)
        self.main_layout.addLayout(self.btn_conv)
        self.main_layout.addLayout(self.tex2_layout)
        self.main_layout.addLayout(self.lcd_display_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = MiniCalculator()
    calculator.show()
    sys.exit(app.exec())