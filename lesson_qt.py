from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QApplication, QLineEdit, QComboBox
import sys

EXCHANGE_RATE = {
    'RUB': 1,
    'USD': 70,
    'EUR': 80,
    'TUB': 30,
}


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Fers program')

        self.main_layout = QHBoxLayout(self)
        self.input_layout = QVBoxLayout(self)
        self.output_layout = QVBoxLayout(self)

        self.input_value = QLineEdit(self)

        self.input_type = QComboBox(self)
        self.input_type.addItems(EXCHANGE_RATE.keys())

        self.convert_button = QPushButton('Convert', self)
        self.convert_button.clicked.connect(self.convert)

        self.output_value = QLineEdit(self)
        self.output_value.setEnabled(False)

        self.output_type = QComboBox(self)
        self.output_type.addItems(EXCHANGE_RATE.keys())

        self.input_layout.addWidget(self.input_value)
        self.input_layout.addWidget(self.input_type)

        self.output_layout.addWidget(self.output_value)
        self.output_layout.addWidget(self.output_type)

        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addLayout(self.convert_button)
        self.main_layout.addLayout(self.output_layout)

        self.setLayout(self.main_layout)

    def convert(self):
        input = float(self.input_value.text()) * EXCHANGE_RATE[self.input_type.currentText()]
        output = input / EXCHANGE_RATE[self.output_type.currentText()]
        self.output_value.setText(f'{output:.2f}')


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
