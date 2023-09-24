import win32api, win32print

from PySide6 import QtWidgets, QtPrintSupport

from controls._messages import shell_execute_error
from dbm import DatabaseModel
from views.print_docx_window import Ui_PrintDocxWindow


class PrintDocxControl(QtWidgets.QMainWindow, Ui_PrintDocxWindow):
    def __init__(self, widget: QtWidgets.QDialog, main, number: int):
        super().__init__()
        self.widget = widget
        self.main = main
        self.number = number
        self.dbm = DatabaseModel()
        self.setupUi(widget)
        self.connectUi()
        self.loadPrinters()
        self.loadData()

    def setupUi(self, widget):
        super().setupUi(widget)
        self.widget.setMaximumWidth(self.widget.width())
        self.widget.setMaximumHeight(self.widget.height())

    def connectUi(self):
        self.cb_contract.stateChanged.connect(lambda state: self.sb_contract_count.setEnabled(state == 2))
        self.cb_act.stateChanged.connect(lambda state: self.sb_act_count.setEnabled(state == 2))
        self.cb_coef.stateChanged.connect(lambda state: self.sb_coef_count.setEnabled(state == 2))
        self.cb_corf1.stateChanged.connect(lambda state: self.sb_corf1_count.setEnabled(state == 2))
        self.cb_corf2.stateChanged.connect(lambda state: self.sb_corf2_count.setEnabled(state == 2))
        self.pb_refresh_printers.clicked.connect(self.loadPrinters)
        self.pb_print.clicked.connect(self.print)

    def loadPrinters(self):
        self.cmb_printers.clear()
        for printer in QtPrintSupport.QPrinterInfo.availablePrinterNames():
            self.cmb_printers.addItem(printer)
        self.cmb_printers.setCurrentText(win32print.GetDefaultPrinter())

    def loadData(self):
        paths = [self.dbm.contracts.get(self.number), self.dbm.acts.get(self.number), self.dbm.ce_orders.get(self.number), self.dbm.cr_orders.get(self.number)]
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
        if self.cmb_printers.currentIndex() != -1:
            if self.cb_contract.isChecked() and self.l_contract_path.text() != f'Путь: -':
                self._print_impl(self.l_contract_path.text()[6:], int(self.sb_contract_count.text()))
            if self.cb_act.isChecked() and self.l_act_path.text() != f'Путь: -':
                self._print_impl(self.l_act_path.text()[6:], int(self.sb_act_count.text()))
            if self.cb_coef.isChecked() and self.l_coef_path.text() != f'Путь: -':
                self._print_impl(self.l_coef_path.text()[6:], int(self.sb_coef_count.text()))
            if self.cb_corf1.isChecked() and self.l_corf1_path.text() != f'Путь: -':
                self._print_impl(self.l_corf1_path.text()[6:], int(self.sb_corf1_count.text()))
            if self.cb_corf2.isChecked() and self.l_corf2_path.text() != f'Путь: -':
                self._print_impl(self.l_corf2_path.text()[6:], int(self.sb_corf2_count.text()))

    def _print_impl(self, docx, count):
        try:
            for _ in range(count):
                win32api.ShellExecute(0, "printto", f'"{docx}"', '"%s"' % self.cmb_printers.currentText(), ".", 0)
        except Exception as e:
            shell_execute_error(e.__str__().translate({ord('\''): None, ord('('): None, ord(')'): None}).split(',')[2], docx)

    def hide_corf2(self):
        self.cb_corf1.setText(f'Приходный кассовый ордер')
        self.cb_corf2.setVisible(False)
        self.l_corf2_path.setVisible(False)
        self.sb_corf2_count.setVisible(False)
