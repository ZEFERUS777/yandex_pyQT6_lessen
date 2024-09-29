from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QLabel
import sys


class Arifmometr(QWidget):
    def __init__(self):
        super(Arifmometr, self).__init__()

        self.main_lay = QHBoxLayout(self)
        self.ed_1_lay = QVBoxLayout(self)
        self.btn_1_lay = QVBoxLayout(self)
        self.btn_2_lay = QVBoxLayout(self)
        self.edi_3_lay = QVBoxLayout(self)
        self.edi_5_lay = QVBoxLayout(self)
        self.edi_6_lay = QVBoxLayout(self)
        self.edi_7_lay = QVBoxLayout(self)

        self.first_value = QLineEdit(self)
        self.first_value.setText('0')
        self.second_value = QLineEdit(self)
        self.second_value.setText('0')

        self.result = QLineEdit(self)
        self.result.setEnabled(False)

        self.add_button = QPushButton('+', self)
        self.add_button.clicked.connect(self.add_button_clicked)
        self.substract_button = QPushButton('-', self)
        self.substract_button.clicked.connect(self.substract_button_clicked)
        self.multiply_button = QPushButton('*', self)
        self.multiply_button.clicked.connect(self.multiply_button_clicked)

        self.lbl_tex = QLabel('=', self)

        self.ed_1_lay.addWidget(self.first_value)
        self.btn_1_lay.addWidget(self.add_button)
        self.btn_2_lay.addWidget(self.substract_button)
        self.edi_3_lay.addWidget(self.multiply_button)
        self.edi_5_lay.addWidget(self.second_value)
        self.edi_6_lay.addWidget(self.lbl_tex)
        self.edi_7_lay.addWidget(self.result)

        self.main_lay.addLayout(self.ed_1_lay)
        self.main_lay.addLayout(self.btn_1_lay)
        self.main_lay.addLayout(self.btn_2_lay)
        self.main_lay.addLayout(self.edi_3_lay)
        self.main_lay.addLayout(self.edi_5_lay)
        self.main_lay.addLayout(self.edi_6_lay)
        self.main_lay.addLayout(self.edi_7_lay)
        self.setLayout(self.main_lay)

    def add_button_clicked(self):
        self.result.setText(str(int(self.first_value.text()) + int(self.second_value.text())))

    def substract_button_clicked(self):
        self.result.setText(str(int(self.first_value.text()) - int(self.second_value.text())))

    def multiply_button_clicked(self):
        self.result.setText(str(int(self.first_value.text()) * int(self.second_value.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Arifmometr()
    window.show()
    sys.exit(app.exec())
