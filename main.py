import datetime
import sys
import traceback

from PySide6.QtWidgets import QApplication, QMainWindow

from controls.main_control import MainControl

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        app.setStyle('Fusion')
        window = QMainWindow()
        control = MainControl(window)
        window.show()
        sys.exit(app.exec())
    except Exception:
        tb = traceback.format_exc()
        print(tb)
        with open('debug.log', 'a') as log:
            log.write(f'{datetime.datetime.now().strftime("%X %x")}\n{tb}\n')
