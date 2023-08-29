import sys
import random
import string
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class PasswordGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Generator')
        self.setGeometry(100, 100, 300, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.password_label = QLabel('Generated Password:')
        layout.addWidget(self.password_label)

        self.password_display = QLineEdit()
        self.password_display.setReadOnly(True)
        layout.addWidget(self.password_display)

        self.length_label = QLabel('Password Length:')
        layout.addWidget(self.length_label)

        self.length_input = QLineEdit()
        layout.addWidget(self.length_input)

        generate_button = QPushButton('Generate Password')
        generate_button.clicked.connect(self.generate_password)
        layout.addWidget(generate_button)

        reset_button = QPushButton('Reset')
        reset_button.clicked.connect(self.reset_password)
        layout.addWidget(reset_button)

        central_widget.setLayout(layout)

    def generate_password(self):
        length = int(self.length_input.text())
        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(characters) for _ in range(length))
        self.password_display.setText(generated_password)

    def reset_password(self):
        self.password_display.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())
