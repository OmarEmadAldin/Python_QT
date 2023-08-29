# Import necessary modules and libraries
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QListWidget, QLineEdit, QVBoxLayout, QWidget, QDialog, QHBoxLayout, QListWidgetItem

# Class for the pop-up window to edit the text in the label
class EditTaskDialog(QDialog):
    def __init__(self, task, parent=None):  # parent is a must param to make the prod acknowledge that this is not the main
        super().__init__(parent)
        self.setWindowTitle('Edit Task')
        self.setGeometry(200, 200, 300, 100)  # Geometry Setup for the pop-up window

        self.layout = QHBoxLayout()

        self.edit_input = QLineEdit()
        self.edit_input.setText(task)
        self.layout.addWidget(self.edit_input)

        self.save_button = QPushButton('Save')
        self.save_button.clicked.connect(self.accept)
        self.layout.addWidget(self.save_button)

        self.setLayout(self.layout)

    def get_edited_task(self):
        return self.edit_input.text()

# Class for the edit button with its branching scenarios
class TaskItemWidget(QWidget):
    def __init__(self, task, parent=None):
        super().__init__(parent)

        self.layout = QHBoxLayout()

        self.task_label = QLineEdit()
        self.task_label.setText(task)
        self.layout.addWidget(self.task_label)

        self.edit_button = QPushButton('Edit')
        self.edit_button.clicked.connect(self.edit_task)
        self.layout.addWidget(self.edit_button)

        self.setLayout(self.layout)

    def edit_task(self):
        edit_dialog = EditTaskDialog(self.task_label.text(), self)
        if edit_dialog.exec_():
            edited_task = edit_dialog.get_edited_task()
            if edited_task:
                self.task_label.setText(edited_task)

# Main class where we implement the whole app
class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('To-Do List')
        self.setGeometry(100, 100, 400, 400)

        self.tasks = []  # List to store tasks

        self.layout = QVBoxLayout()

        self.task_input = QLineEdit()
        self.layout.addWidget(self.task_input)

        self.add_button = QPushButton('Add Task')
        self.add_button.clicked.connect(self.add_task)  # Connect button click to add_task method
        self.layout.addWidget(self.add_button)

        self.delete_button = QPushButton('Delete Selected Task')
        self.delete_button.clicked.connect(self.delete_task)  # Connect button click to delete_task method
        self.layout.addWidget(self.delete_button)

        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    def add_task(self):
        task = self.task_input.text()  # Get text from input field
        if task:
            self.tasks.append(task)  # Add task to the tasks list
            task_widget = TaskItemWidget(task)  # Create a widget to display the task
            item = QListWidgetItem()
            item.setSizeHint(task_widget.sizeHint())
            self.task_list.addItem(item)
            self.task_list.setItemWidget(item, task_widget)  # Associate the widget with the list item
            self.task_input.clear()  # Clear the input field

    def delete_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            row = self.task_list.row(selected_item)  # Get the index of the selected item
            self.tasks.pop(row)  # Remove the task from the tasks list
            self.task_list.takeItem(row)  # Remove the selected item from the list

# Entry point of the program
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the application instance
    TDLApp = ToDoApp()  # Create the main app instance
    TDLApp.task_list.setStyleSheet("background-color: white;")  # Change the background color of the task list
    TDLApp.delete_button.setStyleSheet("background-color: #FF0000; color: white;")  # Change the button color using a gradient

    TDLApp.show()  # Display the main app window
    sys.exit(app.exec_())  # Execute the application and exit on completion
