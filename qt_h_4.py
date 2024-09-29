from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QCheckBox, QApplication
import sys


class WidgetsHideNSeek(QWidget):
    def __init__(self):
        super(WidgetsHideNSeek, self).__init__()
        self.main_layout = QHBoxLayout(self)
        self.check_boxes_layout = QVBoxLayout()
        self.line_edit_layout = QVBoxLayout()

        self.checkbox1 = QCheckBox('edit1', self)
        self.checkbox2 = QCheckBox('edit2', self)
        self.checkbox3 = QCheckBox('edit3', self)
        self.checkbox4 = QCheckBox('edit4', self)

        self.edit1 = QLineEdit(self)
        self.edit1.setPlaceholderText('Поле edit1')
        self.edit2 = QLineEdit(self)
        self.edit2.setPlaceholderText('Поле edit2')
        self.edit3 = QLineEdit(self)
        self.edit3.setPlaceholderText('Поле edit3')
        self.edit4 = QLineEdit(self)
        self.edit4.setPlaceholderText('Поле edit4')

        self.check_boxes_layout.addWidget(self.checkbox1)
        self.check_boxes_layout.addWidget(self.checkbox2)
        self.check_boxes_layout.addWidget(self.checkbox3)
        self.check_boxes_layout.addWidget(self.checkbox4)

        self.line_edit_layout.addWidget(self.edit1)
        self.line_edit_layout.addWidget(self.edit2)
        self.line_edit_layout.addWidget(self.edit3)
        self.line_edit_layout.addWidget(self.edit4)

        self.main_layout.addLayout(self.check_boxes_layout)
        self.main_layout.addLayout(self.line_edit_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = WidgetsHideNSeek()
    widget.show()
    sys.exit(app.exec())