import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from controls.main_control import MainControl

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = QMainWindow()
    control = MainControl(window)
    window.show()
    sys.exit(app.exec())
