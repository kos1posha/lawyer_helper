from PySide6 import QtWidgets, QtCore


class ContractsTableWidgetItem(QtWidgets.QTableWidgetItem):
    def __init__(self, text):
        super().__init__(text)
        self.setFlags(super().flags() ^ QtCore.Qt.ItemFlag.ItemIsEditable)

    def __lt__(self, other):
        try:
            return float(self.text()) < float(other.text())
        except:
            return self.text() < other.text()
