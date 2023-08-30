import sys 
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.result_display = QLineEdit(self)
        self.layout.addWidget(self.result_display)

        buttons = [
            'c', 'S', 'E', '=',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '!', '+'
        ]

        grid_layout = self.create_button_grid(buttons, 4, self.button_clicked)
        self.layout.addLayout(grid_layout)


    def create_button_grid(self, buttons, columns, button_handler):
        layout = QVBoxLayout()
        while buttons:
            row_layout = QHBoxLayout()
            for _ in range(columns):
                if buttons:
                    button_text = buttons.pop(0)
                    button = QPushButton(button_text)
                    button.clicked.connect(lambda text=button_text: button_handler(text))
                    row_layout.addWidget(button)
            layout.addLayout(row_layout)
        return layout
    
    def button_clicked(self, text):
        pass
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyApp = Calculator()
    MyApp.show()
    sys.exit(app.exec_())
