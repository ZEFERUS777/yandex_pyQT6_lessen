from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QApplication, QLineEdit
import sys


class WordTrick(QWidget):
    def __init__(self):  # Changed 'init' to '__init__'
        super(WordTrick, self).__init__()  # Changed 'init' to '__init__'
        self.main_layout = QHBoxLayout(self)
        self.first_lay = QVBoxLayout()
        self.btn_layout = QVBoxLayout()
        self.second_lay = QVBoxLayout()

        self.first_value = QLineEdit(self)
        self.trick_button = QPushButton('->', self)
        self.trick_button.clicked.connect(self.reverse_trick)
        self.second_value = QLineEdit(self)

        self.first_lay.addWidget(self.first_value)
        self.second_lay.addWidget(self.second_value)
        self.btn_layout.addWidget(self.trick_button)

        self.main_layout.addLayout(self.first_lay)
        self.main_layout.addLayout(self.btn_layout)
        self.main_layout.addLayout(self.second_lay)
        self.setLayout(self.main_layout)

    def reverse_trick(self):
        current_first_text = self.first_value.text()
        self.first_value.setText(self.second_value.text())
        self.second_value.setText(current_first_text)

        new_button_text = None
        if self.trick_button.text() == '->':
            new_button_text = '<-'
        else:
            new_button_text = '->'

        self.trick_button.setText(new_button_text)


if __name__ == '__main__':  # Fixed 'name' to '__name__'
    app = QApplication(sys.argv)
    window = WordTrick()
    window.show()
    sys.exit(app.exec())
