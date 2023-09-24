import os, sys, traceback, logging

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

from controls.main_control import MainControl


def excepthook(exc_type, exc_value, exc_tb):
    tb = ''.join(traceback.format_exception(exc_type, exc_value, exc_tb))
    logging.error(tb)
    print(tb)
    QtWidgets.QApplication.quit()


if __name__ == '__main__':
    sys.excepthook = excepthook
    logging.basicConfig(level=logging.ERROR, filename=os.path.abspath('debug.log'), filemode='a', format='[%(asctime)s]\n%(message)s', datefmt='%X %x')
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = QMainWindow()
    control = MainControl(window)
    window.show()
    sys.exit(app.exec())
