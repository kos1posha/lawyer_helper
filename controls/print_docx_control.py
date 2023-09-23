import win32api, win32print

from PySide6 import QtWidgets, QtPrintSupport, QtCore, QtGui

from dbm import DatabaseModel
from views.print_docx_window import Ui_PrintDocxWindow


class PrintDocxControl(QtWidgets.QMainWindow, Ui_PrintDocxWindow):
    def __init__(self, widget: QtWidgets.QDialog, main, number: int):
        super().__init__()
        super().setupUi(widget)
        self.widget = widget
        self.main = main
        self.number = number
        self.dbm = DatabaseModel()
        self.setupUi(widget)
        self.connectUi()
        self.loadPrinters()
        self.loadData()

    def setupUi(self, widget):
        self.widget.setMaximumWidth(self.widget.width())
        self.widget.setMaximumHeight(self.widget.height())

    def connectUi(self):
        self.pb_refresh_printers.clicked.connect(self.loadPrinters)

    def loadPrinters(self):
        self.cmb_printers.clear()
        for printer in QtPrintSupport.QPrinterInfo.availablePrinterNames():
            self.cmb_printers.addItem(printer)

    def loadData(self):
        paths = [
            self.dbm.contracts.get(self.number),
            self.dbm.acts.get(self.number),
            self.dbm.ce_orders.get(self.number),
            self.dbm.cr_orders.get(self.number),
        ]
        self.l_contract_path.setText(f'Путь: {paths[0][-1] if paths[0] else "-"}')
        self.l_act_path.setText(f'Путь: {paths[1][-1] if paths[1] else "-"}')
        self.l_coef_path.setText(f'Путь: {paths[2][-1] if paths[2] else "-"}')
        self.l_corf1_path.setText('Путь: -')
        self.l_corf2_path.setText('Путь: -')
        for path in paths[3]:
            if path[1] == '1': self.l_corf1_path.setText(f'Путь: {path[-1]}')
            else: self.l_corf2_path.setText(f'Путь: {path[-1]}')
        if not paths[0][9]:
            self.hide_corf2()

    def print(self):
        painter = QtGui.QPainter()
        printer = QtPrintSupport.QPrinter()

    def hide_corf2(self):
        self.cb_corf1.setText(f'Приходный кассовый ордер')
        self.cb_corf2.setVisible(False)
        self.l_corf2_path.setVisible(False)
        self.sb_corf2_count.setVisible(False)
