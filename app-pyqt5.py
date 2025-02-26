import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog,
    QLineEdit, QTextEdit, QCheckBox, QRadioButton, QComboBox, QSlider, QProgressBar, QCalendarWidget, QTableWidget,
    QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QListWidget, QSpinBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from qtwidgets import Toggle, PasswordEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("PyQt5 Demo")
        self.setGeometry(100, 100, 1200, 800)
        self.setWindowIcon(QIcon("icons/PyQt5.ico"))

        # Apply Fusion theme
        QApplication.setStyle("Fusion")

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # ============================================================
        # 1. qtwidgets Components
        # ============================================================
        # Toggle Switch
        self.toggle = Toggle()
        layout.addWidget(self.toggle)

        # Password Edit
        self.password_edit = PasswordEdit()
        self.password_edit.setPlaceholderText("Enter password")
        layout.addWidget(self.password_edit)

        # ============================================================
        # 2. Standard PyQt5 Widgets
        # ============================================================
        self.label = QLabel("This is a label")
        layout.addWidget(self.label)

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Enter text")
        layout.addWidget(self.line_edit)

        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Enter multi-line text")
        layout.addWidget(self.text_edit)

        self.checkbox = QCheckBox("Check me")
        layout.addWidget(self.checkbox)

        self.radio1 = QRadioButton("Option 1")
        self.radio2 = QRadioButton("Option 2")
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)

        self.combo_box = QComboBox()
        self.combo_box.addItems(["Item 1", "Item 2", "Item 3"])
        layout.addWidget(self.combo_box)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        layout.addWidget(self.slider)

        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(50)
        layout.addWidget(self.progress_bar)

        self.calendar = QCalendarWidget()
        layout.addWidget(self.calendar)

        self.table = QTableWidget(3, 3)
        self.table.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])
        self.table.setItem(0, 0, QTableWidgetItem("Cell 1"))
        self.table.setItem(1, 1, QTableWidgetItem("Cell 2"))
        layout.addWidget(self.table)

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Item"])
        parent_item = QTreeWidgetItem(["Parent"])
        parent_item.addChild(QTreeWidgetItem(["Child"]))
        self.tree.addTopLevelItem(parent_item)
        layout.addWidget(self.tree)

        self.list_widget = QListWidget()
        self.list_widget.addItem("Item 1")
        self.list_widget.addItem("Item 2")
        layout.addWidget(self.list_widget)

        self.spin_box = QSpinBox()
        self.spin_box.setRange(0, 100)
        layout.addWidget(self.spin_box)

        # ============================================================
        # 3. File Operations
        # ============================================================
        self.open_button = QPushButton("Open File")
        self.open_button.clicked.connect(self.open_file)
        layout.addWidget(self.open_button)

        self.save_button = QPushButton("Save File")
        self.save_button.clicked.connect(self.save_file)
        layout.addWidget(self.save_button)

        # ============================================================
        # 4. Status Bar
        # ============================================================
        self.statusBar().showMessage("Ready")

        # ============================================================
        # 5. Apply QSS Styling
        # ============================================================
        self.apply_styles()

    # ============================================================
    # Open a File
    # ============================================================
    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)")
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.text_edit.setText(content)
                self.statusBar().showMessage(f"Opened: {file_path}")

    # ============================================================
    # Save a File
    # ============================================================
    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*);;Text Files (*.txt)")
        if file_path:
            content = self.text_edit.toPlainText()
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
                self.statusBar().showMessage(f"Saved: {file_path}")

    # ============================================================
    # Apply QSS Styling
    # ============================================================
    def apply_styles(self):
        style_sheet = """
        QMainWindow {
            background-color: #2E3440;
        }
        QLabel {
            color: #D8DEE9;
            font-size: 14px;
        }
        QPushButton {
            background-color: #4C566A;
            color: #D8DEE9;
            border: 1px solid #5E81AC;
            padding: 5px;
            border-radius: 3px;
        }
        QPushButton:hover {
            background-color: #5E81AC;
        }
        QLineEdit, QTextEdit, QComboBox, QSpinBox {
            background-color: #3B4252;
            color: #D8DEE9;
            border: 1px solid #4C566A;
            padding: 5px;
            border-radius: 3px;
        }
        QTabWidget::pane {
            border: 1px solid #4C566A;
            background-color: #3B4252;
        }
        QTabBar::tab {
            background-color: #4C566A;
            color: #D8DEE9;
            padding: 10px;
            border: 1px solid #5E81AC;
            border-bottom: none;
            border-top-left-radius: 3px;
            border-top-right-radius: 3px;
        }
        QTabBar::tab:selected {
            background-color: #5E81AC;
        }
        """
        self.setStyleSheet(style_sheet)


# ============================================================
# Run the Application
# ============================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())