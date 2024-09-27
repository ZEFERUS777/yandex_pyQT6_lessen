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
        self.setFixedSize(270, 90)

        self.input_value = QLineEdit(self)
        self.input_value.move(10, 10)
        self.input_value.resize(100, 30)

        self.input_type = QComboBox(self)
        self.input_type.move(10, 50)
        self.input_type.resize(100, 30)
        self.input_type.addItems(EXCHANGE_RATE.keys())

        self.convert_button = QPushButton('Convert', self)
        self.convert_button.move(120, 10)
        self.convert_button.resize(30, 70)
        self.convert_button.clicked.connect(self.convert)

        self.output_value = QLineEdit(self)
        self.output_value.setEnabled(False)
        self.output_value.move(160, 30)
        self.output_value.resize(100, 30)

        self.output_type = QComboBox(self)
        self.output_type.move(160, 50)
        self.output_type.addItems(EXCHANGE_RATE.keys())
        self.output_type.resize(100, 30)

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
