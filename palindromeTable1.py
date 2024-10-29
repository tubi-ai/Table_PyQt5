from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import (
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, 
    QMessageBox, QPushButton, QLineEdit, QLabel
)

class PalindromeChecker(QWidget):
    def __init__(self, max_size):
        super().__init__()
        self.max_size = max_size  # Maximum allowed index size
        self.list = []  # Store the list of entered strings

        # Window setup
        self.setWindowTitle("Palindrome Checker")
        self.setGeometry(100, 100, 600, 400)

        # Main layout container
        layout = QVBoxLayout()

        # Input section (Text field and Add button)
        self.inputField = QLineEdit()
        self.inputField.setPlaceholderText("Enter a string...")
        self.inputField.setStyleSheet("background-color: #333; color: white; padding: 5px;")

        self.addButton = QPushButton("Add String")
        self.addButton.setStyleSheet("background-color: #5DADE2; color: white; font-weight: bold;")
        self.addButton.clicked.connect(self.add_string)

        layout.addWidget(QLabel("Enter a String:").setStyleSheet("color: white;"))
        layout.addWidget(self.inputField)
        layout.addWidget(self.addButton)

        # Table setup to display strings and their statuses
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Index", "String", "Palindrome?"])
        self.table.setStyleSheet("background-color: #222; color: white;")
        layout.addWidget(self.table)

        # Update section (Field to enter index and Update button)
        self.indexField = QLineEdit()
        self.indexField.setPlaceholderText("Enter index to update...")
        self.indexField.setStyleSheet("background-color: #333; color: white; padding: 5px;")

        self.updateButton = QPushButton("Update Index")
        self.updateButton.setStyleSheet("background-color: #58D68D; color: white; font-weight: bold;")
        self.updateButton.clicked.connect(self.update_index)

        layout.addWidget(QLabel("Enter Index to Update:").setStyleSheet("color: white;"))
        layout.addWidget(self.indexField)
        layout.addWidget(self.updateButton)

        # Set layout and window background color
        self.setLayout(layout)
        self.setStyleSheet("background-color: #2C3E50;")

    def add_string(self):
        """Adds a new string to the list if the size limit is not exceeded."""
        text = self.inputField.text()
        if len(self.list) < self.max_size:
            is_palindrome = "Palindrome" if text == text[::-1] else "Not a Palindrome"
            self.list.append(text)
            self.add_to_table(len(self.list) - 1, text, is_palindrome)
            self.inputField.clear()  # Clear input after adding
        else:
            QMessageBox.warning(self, "Error", "Maximum index reached!")

    def add_to_table(self, index, text, status):
        """Adds a new row to the table with the provided index, text, and palindrome status."""
        self.table.insertRow(index)
        self.table.setItem(index, 0, QTableWidgetItem(str(index)))
        self.table.setItem(index, 1, QTableWidgetItem(text))
        self.table.setItem(index, 2, QTableWidgetItem(status))

        # Apply color styling based on palindrome status
        if status == "Palindrome":
            self.set_row_color(index, QtGui.QColor("#27AE60"))  # Green for palindrome
        else:
            self.set_row_color(index, QtGui.QColor("#C0392B"))  # Red for non-palindrome

    def set_row_color(self, row, color):
        """Sets the background color of a given row."""
        for col in range(3):
            self.table.item(row, col).setBackground(color)

    def update_index(self):
        """Updates the list size based on the entered index."""
        try:
            new_size = int(self.indexField.text())
            if new_size > self.max_size:
                QMessageBox.warning(self, "Error", "Index exceeds the maximum size!")
            elif new_size < len(self.list):
                # Remove rows if the new size is smaller than the current list size
                for i in range(len(self.list) - 1, new_size - 1, -1):
                    self.table.removeRow(i)
                    self.list.pop()
            self.indexField.clear()  # Clear input after updating
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid input!")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = PalindromeChecker(10)  # Set maximum index size to 10
    window.show()
    app.exec_()
