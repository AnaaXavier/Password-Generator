from PySide6.QtWidgets import QApplication, QSlider, QMessageBox, QLabel, QCheckBox, QSpacerItem, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QSizePolicy
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QTimer
from logic import generate_password

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Generator")
        self.setFixedSize(500, 200)

        self.display_password = QLineEdit()
        self.display_password.setPlaceholderText("Password")
        self.display_password.setReadOnly(True)
        self.display_password.setFont(QFont("Arial", 12))
        self.display_password.setFixedHeight(24)

        self.copy_btn = QPushButton("Copy")
        self.copy_btn.setFont(QFont("Arial", 8))
        self.copy_btn.setFixedSize(50, 24)
        self.copy_btn.clicked.connect(self.copy_password)

        self.password_label = QLabel("Password length: 16")
        
        self.password_length_slider = QSlider(Qt.Horizontal)
        self.password_length_slider.setMinimum(1)
        self.password_length_slider.setMaximum(32)
        self.password_length_slider.setValue(16)
        self.password_length_slider.valueChanged.connect(self.update_password_label)
        
        self.include_numbers = QCheckBox("Include numbers")
        self.include_special = QCheckBox("Include special characters")

        self.generate_btn = QPushButton("Generate")
        self.generate_btn.setFont(QFont("Arial", 10))
        self.generate_btn.setFixedSize(100, 45)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.generate_btn)
        self.button_layout.setAlignment(Qt.AlignCenter)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.display_password)
        self.h_layout.addWidget(self.copy_btn)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.h_layout)
        self.main_layout.addWidget(self.password_label)
        self.main_layout.addWidget(self.password_length_slider)
        self.main_layout.addWidget(self.include_numbers)
        self.main_layout.addWidget(self.include_special)
        self.main_layout.addLayout(self.button_layout)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)
        
        self.generate_btn.clicked.connect(self.handle_generation_logic)
        
    def update_password_label(self, value):
        self.password_label.setText(f"Password length: {value}")
    
    def handle_generation_logic(self):
        # It stores the checkboxes' boolean values
        include_numbers = self.include_numbers.isChecked()
        include_special = self.include_special.isChecked()
        password_length = self.password_length_slider.value()

        self.generated_password = generate_password(password_length, include_numbers, include_special)
        self.display_password.setText(self.generated_password)
    
    def copy_password(self):
        # It'll only work if there's a text to copy
        if not self.display_password.text():
            QMessageBox.critical(self, "Error", "A password must be generated to copy.")
            return
        
        clipboard = QApplication.clipboard()
        clipboard.setText(self.display_password.text())

        self.copy_btn.setText("Copied")
        self.copy_btn.setEnabled(False)

        QTimer.singleShot(2000, self.reset_copy_button)
    
    # The button will be back again once the timer ends
    def reset_copy_button(self):
        self.copy_btn.setText("Copy")
        self.copy_btn.setEnabled(True)

if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    window.show()
    app.exec()
