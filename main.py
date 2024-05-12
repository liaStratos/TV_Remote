import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from TV_logic import Television

if __name__ == "__main__":
    app = QApplication(sys.argv)

    tv = Television()

    window = QMainWindow()

    window.setCentralWidget(tv)

    window.setWindowTitle("TV_Remote")
    window.show()

    sys.exit(app.exec())

