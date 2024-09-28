from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
import sys


class Evaluator(QWidget):
    def __init__(self):  # Исправлено на __init__
        super(Evaluator, self).__init__()  # Исправлено на __init__
        self.main_layout = QHBoxLayout(self)
        self.first_lay = QVBoxLayout()
        self.btn_layout = QVBoxLayout()
        self.second_lay = QVBoxLayout()

        self.first_value = QLineEdit(self)
        self.trick_button = QPushButton('->', self)
        self.trick_button.clicked.connect(self.trick_button_clicked)
        self.second_value = QLineEdit(self)

        self.first_lay.addWidget(self.first_value)
        self.btn_layout.addWidget(self.trick_button)
        self.second_lay.addWidget(self.second_value)
        self.main_layout.addLayout(self.first_lay)
        self.main_layout.addLayout(self.btn_layout)
        self.main_layout.addLayout(self.second_lay)
        self.setLayout(self.main_layout)

    def trick_button_clicked(self):
        try:
            curr = eval(self.first_value.text())
            self.second_value.setText(str(curr))  # Приведено к строке
        except Exception as e:
            self.second_value.setText("Ошибка")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    evaluator = Evaluator()
    evaluator.show()
    sys.exit(app.exec())
